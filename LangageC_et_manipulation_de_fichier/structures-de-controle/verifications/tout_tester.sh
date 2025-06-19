#!/bin/bash

declare -a noms_tests
declare -a etats_tests

declare nb_tests_effectues
declare nb_tests_reussis
declare nb_tests_echoues

nb_tests_effectues=0
nb_tests_reussis=0
nb_tests_echoues=0

tester(){
    programme=$1
    shift
    args="$@"
    noms_tests+=("$programme $args")
    
    if $programme $args > /dev/null
    then
        echo "test $programme $args OK"
        (( nb_tests_reussis++ ))
        etats_tests+=("OK")
    else
        echo "test $programme $args KO"
        (( nb_tests_echoues++ ))
        etats_tests+=("KO")
    fi
}

#         programme                        arguments      reference
tester ./pair_impair_verification.sh          15 reference_impair.txt
tester ./pair_impair_verification.sh          57 reference_impair.txt
tester ./pair_impair_verification.sh          56 reference_pair.txt
tester ./pair_impair_verification.sh          29 reference_pair.txt
tester ./pair_impair_verification.sh          30548 reference_impair.txt
tester ./pair_impair_verification.sh          5459 reference_pair.txt
tester ./test_demoparam.sh                    reference_demoparam1 a b c d e f
tester ./test_demoparam.sh                    reference_demoparam1 a b c d e

(( nb_tests_effectues = nb_tests_reussis + nb_tests_echoues ))

echo "nb_tests_effectues = $nb_tests_effectues"
echo "nb_tests_reussis = $nb_tests_reussis"
echo "nb_tests_echoues = $nb_tests_echoues"

for (( i=0; i<${#noms_tests[@]}; i++ ))
do
    echo "|   ${noms_tests[$i]}   |  ${etats_tests[$i]}  |"
done
