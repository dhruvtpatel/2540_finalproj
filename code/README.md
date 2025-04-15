# 2540_finalproj

functions.py: contains our dataset of original functions
classify_difficulty.py: code to classify the difficulty of programs in our dataset

/code: all code

    /functions: all files related to our generated functions
        functions.py: the original 45 functions
        functions_with_assertions.py: functions with assertions moved earlier by LLM
        transformed_functions.py: transformed function that checks if early and final assertions are equivalent
        symbolic_execution_specs.py: functions in a format useable by CrossHair

    classify_difficulty.py: script to generate the difficulty ratings for all programs

    /verification: scripts to verify the programs work using 3 approaches: crosshair, fuzzy, nagini

    
/results
    fuzz_results.txt: results for fuzzy testing all of the functions
    crosshair_results.txt: results for using CrossHair symbolic execution