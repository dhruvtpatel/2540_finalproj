This page shows examples of information flow specifications in Nagini. More full examples can be found [here](https://github.com/marcoeilers/nagini/tree/esop/tests/sif/verification/examples) and [here](https://github.com/marcoeilers/nagini/tree/esop/tests/sif/verification/secc).

## Basic contracts

Nagini specifications are based on implicit dynamic frames, a logic similar to separation logic. The separation logic assertion 
``e.f |-> v``, which specifies both a permission to the field ``e.f`` and the information that its value is ``v``, is split into two parts in Nagini: The permission can be expressed as ``Acc(e.f)``, and the value information can optionally be added by specifying ``e.f is v``. 

Information flow can be expressed via the assertion ``Low(e)``, which expresses that ``e`` is low, and ``LowEvent()``, which specifies that the current control flow (i.e. the program counter) is low. 

A precondition stating that one requires a permission to ``e.f`` and that its value must be low can thus be written as ``Requires(Acc(e.f) and Low(e.f))``.

The following code from the "Darvas" example shows an example with simple specifications:
```python
from nagini_contracts.contracts import *

class Account():
    def __init__(self) -> None:
        self.balance = 0
        self.extraService = False

    def writeBalance(self, amount: int) -> None:
        # balance and amount are high -> low extraService reveals information about high variable
        Requires(Acc(self.balance))
        Requires(Acc(self.extraService))
        Requires(Low(self.extraService))
        Ensures(Acc(self.balance))
        Ensures(Acc(self.extraService))
        Ensures(Low(self.extraService))  # FAILS!
        if amount >= 10000:
            self.extraService = True
        else:
            self.extraService = False
        self.balance = amount

    def writeBalance_fixed(self, amount: int) -> None:
        Requires(Acc(self.balance))
        Requires(Acc(self.extraService))
        Requires(Low(self.extraService))
        Ensures(Acc(self.balance))
        Ensures(Acc(self.extraService))
        Ensures(Low(self.extraService))
        Declassify(amount >= 10000)      # SUCCEEDS because of declassification
        if amount >= 10000:
            self.extraService = True
        else:
            self.extraService = False
        self.balance = amount

    def readBalance(self) -> int:
        Requires(Acc(self.balance))
        Ensures(Acc(self.balance))
        return self.balance

    def readExtra(self) -> bool:
        Requires(Acc(self.extraService))
        Ensures(Acc(self.extraService))
        return self.extraService
```


In method ``writeBalance_fixed``, this code also uses the declassification statement ``Declassify(e)``, which declassifies the value of ``e``.

## Lock invariants and value-dependent specifications

The following example (SecC CAV) shows concurrent code that uses a lock. Locks have to declare an invariant (by defining a predicate named 'invariant') that describes the permissions held by the lock. Lock invariants (like all predicates) can contain information flow assertions. This invariant can refer to the object protected by the lock via the ``get_locked()`` function. Acquiring the lock gives a thread the permissions in the lock, and releasing it forces it to give them back and reestablish the invariant.

In the example, the lock invariant contains a value-dependent specification: ``Implies(not self.get_locked().is_classified, Low(self.get_locked().data))`` means that the locked object's ``data`` field is low **if** its ``is_classified`` field is true, i.e., that its sensitivity depends on the value of the ``is_classified`` field.

```python
from nagini_contracts.contracts import *
from nagini_contracts.lock import Lock

class Record:
    def __init__(self, ic: bool, data: int) -> None:
        self.is_classified = ic
        self.data = data


class Mutex(Lock[Record]):

    @Predicate
    def invariant(self) -> bool:
        return (Acc(self.get_locked().is_classified) and
                Acc(self.get_locked().data) and
                Low(self.get_locked().is_classified) and
                Implies(not self.get_locked().is_classified, Low(self.get_locked().data)))


# Models OUTPUT_REG from the SecCSL paper
def output(i: int) -> None:
    Requires(Low(i))


def thread1(r: Record, m: Mutex) -> None:
    Requires(m.get_locked() is r and Low(m))
    while True:
        m.acquire()
        if not r.is_classified:
            output(r.data)
        m.release()


def thread2(r: Record, m: Mutex) -> None:
    Requires(m.get_locked() is r and Low(m))
    m.acquire()
    r.is_classified = False
    r.data = 0
    m.release()


def thread1_insecure(r: Record, m: Mutex) -> None:
    Requires(m.get_locked() is r and Low(m))
    while True:
        m.acquire()
        if r.is_classified:  # BUG
            output(r.data)
        m.release()


def thread2_insecure(r: Record, m: Mutex) -> None:
    Requires(m.get_locked() is r and Low(m))
    m.acquire()
    r.is_classified = False
    # BUG: r.data = 0
    m.release()
```

