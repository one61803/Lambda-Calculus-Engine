import random
"""
>>> is_well_formed("(λx.x) (λx.x)") => False
>>> is_well_formed("((λx.x) (λx.x))") => True
Alpha-replace only:
>>> lambda_process("((λx.x) (λx.x))") => '((λLPQ.LPQ) (λx.x))'
Beta-reduction:
>>> lambda_process("((λx.x) y)") => 'y'
>>> lambda_process("(((λx.(λy.x)) 1) 2)") => '1'
>>> lambda_process("(((λx.(λy.y)) 1) 2)") => '2'
>>> lambda_process("((((λa.(λb.(λm.((m a) b)))) 10) 20) (λx.(λy.x)))") => 10
>>> lambda_process("((λm.((m 10) 20)) (λx.(λy.x)))") => 10
>>> lambda_process("((((λa.(λb.(λm.((m a) b)))) 10) 20) (λx.(λy.y)))") => 20
>>> lambda_process("((λn.(λf.(λx.(f ((n f) x))))) (λf.(λx.(f x))))") => '(λEKT.(λFHC.(EKT (EKT FHC))))'
>>> lambda_process("((λn.(λf.(λx.(f ((n f) x))))) (λf.(λx.(f (f x)))))") => '(λALV.(λNKT.(ALV (ALV (ALV NKT)))))'

Version 2:
lambda_stamps("(SUCC ONE)")
'((λn.(λf.(λx.(f ((n f) x))))) (λf.(λx.(f x))))'
lambda_process('((λn.(λf.(λx.(f ((n f) x))))) (λf.(λx.(f x))))')
'(λFSE.(λKQN.(FSE (FSE KQN))))'

lambda_stamps("(SUCC TWO)")
'((λn.(λf.(λx.(f ((n f) x))))) (λf.(λx.(f (f x)))))'
lambda_process('((λn.(λf.(λx.(f ((n f) x))))) (λf.(λx.(f (f x)))))')
'(λZEF.(λYGH.(ZEF (ZEF (ZEF YGH)))))'

lambda_stamps("(SUCC THREE)")
'((λn.(λf.(λx.(f ((n f) x))))) (λf.(λx.(f (f (f x))))))'
lambda_process('((λn.(λf.(λx.(f ((n f) x))))) (λf.(λx.(f (f (f x))))))')
'(λSTV.(λGZG.(STV (STV (STV (STV GZG))))))'

lambda_stamps("((ADD ONE) ONE)")
'(((λa.(λb.((a (λn.(λf.(λx.(f ((n f) x)))))) b))) (λf.(λx.(f x)))) (λf.(λx.(f x))))'
lambda_process('(((λa.(λb.((a (λn.(λf.(λx.(f ((n f) x)))))) b))) (λf.(λx.(f x)))) (λf.(λx.(f x))))')
'(λMGW.(λRGN.(MGW (MGW RGN))))'

lambda_stamps("((ADD TWO) TWO)")
'(((λa.(λb.((a (λn.(λf.(λx.(f ((n f) x)))))) b))) (λf.(λx.(f (f x))))) (λf.(λx.(f (f x)))))'
lambda_process('(((λa.(λb.((a (λn.(λf.(λx.(f ((n f) x)))))) b))) (λf.(λx.(f (f x))))) (λf.(λx.(f (f x)))))')
'(λJMX.(λOFP.(JMX (JMX (JMX (JMX OFP))))))'

lambda_process(lambda_stamps("((ADD TWO) THREE)"))
'(λXEA.(λNWN.(XEA (XEA (XEA (XEA (XEA NWN)))))))'

lambda_process(lambda_stamps("((MULT TWO) TWO)")
'(λMRH.(λRPP.(MRH (MRH (MRH (MRH RPP))))))'

lambda_process("((λb.((λNKX.((b (λn.(λOIU.(λEZS.(OIU ((n OIU) EZS)))))) ((b (λn.(λOIU.(λEZS.(OIU ((n OIU) EZS)))))) NKX))) \
(λFST.(λXZA.XZA)))) (λf.(λx.(f (f x)))))")
'(λOIU.(λEZS.(OIU (OIU (OIU (OIU EZS))))))'

lambda_process(lambda_stamps("((MULT TWO) THREE)"))
'(λYQR.(λSFD.(YQR (YQR (YQR (YQR (YQR (YQR SFD))))))))'

lambda_process(lambda_stamps("((MULT THREE) THREE)"))
'(λBJQ.(λHUA.(BJQ (BJQ (BJQ (BJQ (BJQ (BJQ (BJQ (BJQ (BJQ HUA)))))))))))'

lambda_process(lambda_stamps("(CAR ((CONS 12) 20))"))
'12'

lambda_process(lambda_stamps("(CDR ((CONS 12) 20))"))
'20'

>>> lambda_process(lambda_stamps("(PRED THREE)"))
???

>>> lambda_process(lambda_stamps("(PRED TWO)"))
'(λBRN.(λTTD.(BRN TTD)))'

>>> lambda_process("((λF.FZJ) (λF.F))")
'FZJ'

>>> lambda_process(lambda_stamps("(PRED THREE)"))                                                                                                                                                                                             
'(λLDI.(λGOT.(LDI (LDI GOT))))'
"""

def is_well_formed(string_ST):
    string_ST = string_ST.replace("A", "_")
    string_ST = string_ST.replace("B", "_")
    string_ST = string_ST.replace("C", "_")
    string_ST = string_ST.replace("D", "_")
    string_ST = string_ST.replace("E", "_")
    string_ST = string_ST.replace("F", "_")
    string_ST = string_ST.replace("G", "_")
    string_ST = string_ST.replace("H", "_")
    string_ST = string_ST.replace("I", "_")
    string_ST = string_ST.replace("J", "_")
    string_ST = string_ST.replace("K", "_")
    string_ST = string_ST.replace("L", "_")
    string_ST = string_ST.replace("M", "_")
    string_ST = string_ST.replace("N", "_")
    string_ST = string_ST.replace("O", "_")
    string_ST = string_ST.replace("P", "_")
    string_ST = string_ST.replace("Q", "_")
    string_ST = string_ST.replace("R", "_")
    string_ST = string_ST.replace("S", "_")
    string_ST = string_ST.replace("T", "_")
    string_ST = string_ST.replace("U", "_")
    string_ST = string_ST.replace("V", "_")
    string_ST = string_ST.replace("W", "_")
    string_ST = string_ST.replace("X", "_")
    string_ST = string_ST.replace("Y", "_")
    string_ST = string_ST.replace("Z", "_")
    string_ST = string_ST.replace("a", "_")
    string_ST = string_ST.replace("b", "_")
    string_ST = string_ST.replace("c", "_")
    string_ST = string_ST.replace("d", "_")
    string_ST = string_ST.replace("e", "_")
    string_ST = string_ST.replace("f", "_")
    string_ST = string_ST.replace("g", "_")
    string_ST = string_ST.replace("h", "_")
    string_ST = string_ST.replace("i", "_")
    string_ST = string_ST.replace("j", "_")
    string_ST = string_ST.replace("k", "_")
    string_ST = string_ST.replace("l", "_")
    string_ST = string_ST.replace("m", "_")
    string_ST = string_ST.replace("n", "_")
    string_ST = string_ST.replace("o", "_")
    string_ST = string_ST.replace("p", "_")
    string_ST = string_ST.replace("q", "_")
    string_ST = string_ST.replace("r", "_")
    string_ST = string_ST.replace("s", "_")
    string_ST = string_ST.replace("t", "_")
    string_ST = string_ST.replace("u", "_")
    string_ST = string_ST.replace("v", "_")
    string_ST = string_ST.replace("w", "_")
    string_ST = string_ST.replace("x", "_")
    string_ST = string_ST.replace("y", "_")
    string_ST = string_ST.replace("z", "_")
    string_ST = string_ST.replace("1", "_")
    string_ST = string_ST.replace("2", "_")
    string_ST = string_ST.replace("3", "_")
    string_ST = string_ST.replace("4", "_")
    string_ST = string_ST.replace("5", "_")
    string_ST = string_ST.replace("6", "_")
    string_ST = string_ST.replace("7", "_")
    string_ST = string_ST.replace("8", "_")
    string_ST = string_ST.replace("9", "_")
    string_ST = string_ST.replace("0", "_")

    while "__" in string_ST:
        string_ST = string_ST.replace("__", "_")

    continue_BL = True
    while continue_BL:
        continue_BL = False
        if "(_ _)" in string_ST:
            string_ST = string_ST.replace("(_ _)", "=")
            continue_BL = True
        if "(= _)" in string_ST:
            string_ST = string_ST.replace("(= _)", "=")
            continue_BL = True
        if "(_ =)" in string_ST:
            string_ST = string_ST.replace("(_ =)", "=")
            continue_BL = True
        if "(= =)" in string_ST:
            string_ST = string_ST.replace("(= =)", "=")
            continue_BL = True
        if "(λ_._)" in string_ST:
            string_ST = string_ST.replace("(λ_._)", "=")
            continue_BL = True
        if "(λ_.=)" in string_ST:
            string_ST = string_ST.replace("(λ_.=)", "=")
            continue_BL = True
        DEBUG(debug_11, f"string_ST: {string_ST}")

    return (string_ST == "_") or (string_ST == "=")
        
"""Idea for detecting when to beta-reduce: do parentheses-counting. Scan the characters in the string from left to right. There should be a 'height_LS'
array which would indicate how high a position of the string is. An open parenthesis increases the height_NT by 1. A close parentheses decreases the
height count by 1, but with a position delay of 1. There should also be a 'terrace' array. When the height at position `i` is determined to be `n`, then
if the character at `i` is non-alphanumeric, then let terrace[n] += string_ST[i]. If the character is λ then let position_NT = i - 2.  When the
pattern "((λ.) )" (or "((λ.) ") is detected at the end of a terrace, then a beta reduction can be applied at that height."""

"""How to detect when to alpha-replace? (All alpha-replacements should be done previous to any beta-reduction, just in case.) Scan the characters in
string_ST from left to right while counting parentheses. When a λ shows up, let its position+1 be stored in position_NT and start storing the
characters right after it in variable_ST until a . is reached.
[[Then store {variable_ST, position_NT} in associative array, unless there is already
a pair with key variable_ST.]]
[[Then store variable_ST in variables_LS, unless variables_LS already contains an item that is identical to variable_ST, in which case the variable at
position_NT should be alpha-replaced.]]
Then store {variable_ST: [(position_NT, height_NT)]} in dictionary variables_DC, unless there is an
entry already with key variable_ST, in which case append the pair (position_NT, height_NT) to the body of the entry. At the end of the scanning,
look at each entry in the dictionary. If a body has more than one pair then pick a pair with the maximum height for the list in that body.
(If more than one pair have that same height then just pick one such pair.)"""

"""How to alpha-replace? Let alpha_open_NT = position_NT, alpha_height_NT = height_NT, alpha_variable_ST = variable_ST. Scan the string starting at
alpha_open_NT and counting parentheses; find out when a closing parenthesis first shows up at alpha_height_NT. Store that in alpha_close_NT.
Randomly pick an alpha_replace_ST that is three capital letters. Now find instances of alpha_variable_ST located between alpha_open_NT and alpha_close_NT and
replace them with alpha_replace_ST."""

"""How to beta-reduce? Let beta_open_NT = position_NT (when the possibility of a beta-reduction has been detected). Let
beta_height_1_NT = height_LS[position_NT]. Let beta_height_2_NT = beta_height_1_NT + 1. Look for the first . after the λ at beta_open_NT+1. Store
its position in beta_dot_NT. Store the name between λ and . in beta_variable_ST. Keep scanning the string rightwards and counting parentheses
until reaching the first closing parenthesis at height beta_height_2_NT. There should be a space right after it; store its position at beta_space_NT.
Keep scanning the string rightwards and counting parentheses until reaching the first closing parenthesis at beta_height_1_NT; store its position in
beta_close_NT.

Replace the beta_variable_ST between beta_open_NT+4 and beta_dot_NT with a '#' character. [[Right afterwards, replace all other occurrences of
beta_variable_ST with '_'. (Note: due to the previous alpha-replacements, there should not be a problem with doing this.]] [Wrong: what about unbounded
variables? ]) Replace occurrences of beta_variable_ST between beta_dot_NT and beta_space_NT with an '_'. Store the part of the string between
beta_space_NT and beta_close_NT in beta_replacer_ST. Replace that part of the string (equal to beta_replacer_ST) with a "*". Replace all occurrences of '_'
with beta_replacer_ST. Now replace '((λ#.' with '' and replace ') *)' with ''. That is it; the beta-reduction should be done.

((λ#.==^^===^^===) *)
==^^===^^==="""

def maximum_height(string_ST):
    height_NT = 0
    max_height_NT = -1
    for i in range(len(string_ST)):
        if (string_ST[i] == "("):
            height_NT += 1
            if (height_NT > max_height_NT):
                max_height_NT = height_NT
        elif (string_ST[i] == ")"):
            height_NT -= 1
    return max_height_NT

def DEBUG(flag, msg_ST):
    "{...}"
    if flag:
        print(msg_ST)

debug_1 = False
debug_2 = False
debug_3 = False
debug_4 = False
debug_5 = False
debug_6 = False
debug_7 = False
debug_8 = False
debug_9 = False
debug_10 = False
debug_11 = False
debug_12 = False

def lambda_process(string_ST):
    if not is_well_formed(string_ST):
        print("Error: the given formula is not well-formed.")
        quit()
    string_ST = alpha_replacement(string_ST)
    "beta-reduction"
    beta_BL = True
    while beta_BL:
        beta_BL = False
        height_LSNT = [0] * len(string_ST)
        height_NT = 0
        position_NT = -1    # unemployed
        terrace_LSST = [""] * (maximum_height(string_ST) + 2)
        lambda_pos_LSNT = [-1] * (maximum_height(string_ST) + 1)
        for i in range(len(string_ST)):
            DEBUG(debug_2, f"i = {i}")
            if (string_ST[i] == "("):
                height_NT += 1
            elif (i > 0) and (string_ST[i - 1] == ")"):
                height_NT -= 1
            height_LSNT[i] = height_NT
            if (string_ST[i] in ["(", ")", " ", "λ", "."]):
                terrace_LSST[height_NT] += string_ST[i]
                DEBUG(debug_2, f"height_NT = {height_NT}; terrace_LSST[height_NT] = {terrace_LSST[height_NT]}")
                if (string_ST[i] == "λ"):
                    #position_NT = i - 2
                    DEBUG(debug_1, f"height_NT = {height_NT}; i = {i}")
                    lambda_pos_LSNT[height_NT] = i
                elif (string_ST[i] == " ") and not beta_BL:
                    #if (terrace_LSST[height_NT] == "((λ.) "):
                    DEBUG(debug_8, "- - - - - - - - - - - - - - - - - - - -")
                    DEBUG(debug_8, f"L297. height_NT = {height_NT}")
                    DEBUG(debug_8, f"L298. string_ST     = {string_ST}")
                    DEBUG(debug_8, f"L299. i = {i}")
                    DEBUG(debug_8, f"L300. string_ST[:i] = {string_ST[:i]}")
                    DEBUG(debug_8, f"terrace_LSST[height_NT] = {terrace_LSST[height_NT]}")
                    DEBUG(debug_8, f"terrace_LSST[height_NT + 1] = {terrace_LSST[height_NT + 1]}")
                    if (len(terrace_LSST[height_NT]) >= 2) and (terrace_LSST[height_NT][-2:] == "( ") \
                       and (len(terrace_LSST[height_NT + 1]) >= 4) and (terrace_LSST[height_NT + 1][-4:] == "(λ.)"):
                        beta_BL = True
                        #beta_open_NT = position_NT
                        DEBUG(debug_2, f"beta_BL = {beta_BL}")
                        DEBUG(debug_3, f"L308. i = {i}")
                        DEBUG(debug_3, f"height_LSNT[i] = {height_LSNT[i]}")
                        DEBUG(debug_3, f"height_NT = {height_NT}")
                        #beta_height_1_NT = height_LSNT[position_NT]
                        beta_height_1_NT = height_NT
                        beta_height_2_NT = beta_height_1_NT + 1
                        beta_open_NT = lambda_pos_LSNT[beta_height_2_NT] - 2
                        beta_lambda_NT = lambda_pos_LSNT[beta_height_2_NT]
                        DEBUG(debug_3, f"L316. beta_height_2_NT = {beta_height_2_NT}")
                        DEBUG(debug_3, f"lambda_pos_LSNT[beta_height_2_NT] = {lambda_pos_LSNT[beta_height_2_NT]}")
                        DEBUG(debug_8, f"L318. beta_open_NT = {beta_open_NT}")
                        DEBUG(debug_8, f"L319. beta_lambda_NT = {beta_lambda_NT}")
                elif (string_ST[i] == ")"):
                    terrace_LSST[height_NT + 1] = ""
        "If beta_BL is True then there is a beta-reduction to be done."
        if beta_BL:
            height_NT = beta_height_1_NT - 1
            DEBUG(debug_8, "= = = = = = = = = = = = = = = = = = = =")            
            DEBUG(debug_4, f"L370. beta_height_1_NT = {beta_height_1_NT}")
            DEBUG(debug_8, f"L371. string_ST = {string_ST}")
            DEBUG(debug_8, f"L372. _________ = {beta_open_NT*'/' + string_ST[beta_open_NT : ]}")
            DEBUG(debug_8, f"L373. beta_open_NT = {beta_open_NT}")
            DEBUG(debug_8, f"L374. beta_lambda_NT = {beta_lambda_NT}")
            beta_dot_NT = -1
            beta_space_NT = -1            
            beta_close_NT = -1
            DEBUG(debug_8, f"L378. beta_space_NT = {beta_space_NT}")
            DEBUG(debug_8, f"L379. beta_close_NT = {beta_close_NT}")
            for i in range(beta_open_NT, len(string_ST)):
                DEBUG(debug_4, f"L381. i = {i} ; {string_ST[ : i]}")
                if (string_ST[i] == "("):
                    height_NT += 1
                    DEBUG(debug_4, f"L384. height_NT = {height_NT}")
                elif (i > 0) and (string_ST[i - 1] == ")"):
                    height_NT -= 1
                    DEBUG(debug_4, f"L387. height_NT = {height_NT}")
                if (string_ST[i] == ".") and (height_NT == beta_height_2_NT):
                    if (beta_space_NT == -1):
                        beta_dot_NT = i
                        DEBUG(debug_8, f"L391. beta_dot_NT = {beta_dot_NT}")
                elif (string_ST[i] == " ") and (height_NT == beta_height_1_NT):
                    beta_space_NT = i
                    DEBUG(debug_8, f"L394. beta_space_NT = {beta_space_NT}")
                elif (string_ST[i] == ")") and (height_NT == beta_height_1_NT):
                    beta_close_NT = i
                    DEBUG(debug_8, f"L397. beta_close_NT = {beta_close_NT}")
                    break
            beta_variable_ST = string_ST[beta_lambda_NT + 1 : beta_dot_NT]
            DEBUG(debug_6, f"L412. beta_variable_ST = {beta_variable_ST}")
            string_ST = string_ST[ : beta_lambda_NT + 1] + "#"*len(beta_variable_ST) + string_ST[beta_dot_NT : ]
            for i in range(beta_dot_NT + 1, beta_space_NT):
                if (string_ST[i : i + len(beta_variable_ST)] == beta_variable_ST):
                    string_ST = string_ST[ : i] + "_"*len(beta_variable_ST) + string_ST[i + len(beta_variable_ST) : ]
            beta_replacer_ST = string_ST[beta_space_NT + 1 : beta_close_NT]
            string_ST = string_ST[ : beta_space_NT + 1] + "*" + string_ST[beta_close_NT : ]
            while "##" in string_ST:
                string_ST = string_ST.replace("##", "#")
            while "__" in string_ST:
                string_ST = string_ST.replace("__", "_")
            DEBUG(debug_8, f"L423. string_ST = {string_ST}")
            string_ST = string_ST.replace("_", beta_replacer_ST)
            string_ST = string_ST.replace("((λ#.", "")
            string_ST = string_ST.replace(") *)", "")
            DEBUG(debug_8 or debug_9, f"L427. string_ST = {string_ST} <<<<<<<<<<<<<<<<<<<<<<<<<<<")
            if not is_well_formed(string_ST):
                DEBUG(debug_10, f"L429. string_ST = {string_ST}")
                print("L430. ERROR: the string resulting from the latest beta-reduction is not well-formed.")
                quit()
            string_ST = alpha_replacement(string_ST)
    return string_ST

def lambda_stamps(string_ST):
    continue_BL = True
    while continue_BL:
        continue_BL = False
        if "TRUE" in string_ST:
            string_ST = string_ST.replace("TRUE", "(λT.(λF.T))")
            continue_BL = True
        elif "FALSE" in string_ST:
            string_ST = string_ST.replace("FALSE", "(λT.(λF.F))")
            continue_BL = True
        elif "CONS" in string_ST:
            string_ST = string_ST.replace("CONS", "(λa.(λb.(λm.((m a) b))))")
            continue_BL = True
        elif "CAR" in string_ST:
            string_ST = string_ST.replace("CAR", "(λp.(p TRUE))")
            continue_BL = True
        elif "CDR" in string_ST:
            string_ST = string_ST.replace("CDR", "(λp.(p FALSE))")
            continue_BL = True
        elif "ZERO" in string_ST:
            "Note: ZERO is meant to be used as a Church numeral, but it is isomorphic to FALSE."
            string_ST = string_ST.replace("ZERO", "(λf.(λx.x))")
            continue_BL = True
        elif "ONE" in string_ST:
            string_ST = string_ST.replace("ONE", "(λf.(λx.(f x)))")
            continue_BL = True
        elif "TWO" in string_ST:
            string_ST = string_ST.replace("TWO", "(λf.(λx.(f (f x))))")
            continue_BL = True
        elif "THREE" in string_ST:
            string_ST = string_ST.replace("THREE", "(λf.(λx.(f (f (f x)))))")
            continue_BL = True
        elif "SUCC" in string_ST:
            string_ST = string_ST.replace("SUCC", "(λn.(λf.(λx.(f ((n f) x)))))")
            continue_BL = True
        elif "ADD" in string_ST:
            string_ST = string_ST.replace("ADD", "(λa.(λb.((a SUCC) b)))")
            continue_BL = True
        elif "MULT" in string_ST:
            string_ST = string_ST.replace("MULT", "(λa.(λb.((a (ADD b)) ZERO)))")
            continue_BL = True
        elif "PRED" in string_ST:
            string_ST = string_ST.replace("PRED", "(λn.(CDR ((n (λp.((CONS (SUCC (CAR p))) (CAR p)))) ((CONS ZERO) ZERO))))")
            continue_BL = True
    return string_ST

def lambda_test(number_NT):
    match number_NT:
        case 1:
            lambda_process("((λb.((λNKX.((b (λn.(λOIU.(λEZS.(OIU ((n OIU) EZS)))))) ((b (λn.(λOIU.(λEZS.(OIU ((n OIU) EZS)))))) NKX))) \
(λFST.(λXZA.XZA)))) (λf.(λx.(f (f x)))))")
        case 2:
            lambda_process(lambda_stamps("(PRED THREE)"))

def alpha_replacement(string_ST):
    alpha_BL = True
    while alpha_BL:
        height_LS = [0] * len(string_ST)
        height_NT = 0
        variables_DC = {}
        variable_BL = False
        for i in range(len(string_ST)):
            if (string_ST[i] == "("):
                height_NT += 1
            elif (i > 0) and (string_ST[i - 1] == ")"):
                height_NT -= 1
            height_LS[i] = height_NT
            if (string_ST[i] == "λ"):
                position_NT = i + 1
                variable_ST = ""
                variable_BL = True
            elif (string_ST[i] == "."):
                variable_BL = False
                if not (variable_ST in variables_DC):
                    variables_DC[variable_ST] = [(position_NT, height_NT)]
                else:
                    what_LS = variables_DC[variable_ST]
                    what_LS += [(position_NT, height_NT)]
                    variables_DC[variable_ST] = what_LS
            elif variable_BL:
                variable_ST += string_ST[i]
        alpha_BL = False
        variable_to_replace_ST = ""
        for key_ST in variables_DC:
            if (len(variables_DC[key_ST]) > 1) and not alpha_BL:
                alpha_BL = True
                variable_to_replace_ST = key_ST
                max_height_NT = -1
                max_position_NT = -1
                for pair_OP in variables_DC[key_ST]:
                    if (pair_OP[1] > max_height_NT):
                        max_height_NT = pair_OP[1]
                        max_position_NT = pair_OP[0]
        "If alpha_BL is True then an alpha-replacement needs to be done."
        if alpha_BL:
            alpha_open_NT = max_position_NT
            alpha_height_NT = max_height_NT
            alpha_variable_ST = variable_to_replace_ST
            not_closed_BL = True
            i = alpha_open_NT + 1
            height_NT = alpha_height_NT
            DEBUG(debug_12, f"L292. alpha_open_NT = {alpha_open_NT}")
            DEBUG(debug_12, f"L293. alpha_variable_ST = {alpha_variable_ST}")
            DEBUG(debug_12, f"L294. string_ST                = {string_ST}")
            while not_closed_BL:
                if (string_ST[i] == "("):
                    height_NT += 1
                if (i > 0) and (string_ST[i - 1] == ")"):
                    height_NT -= 1
                if (string_ST[i] == ")") and (height_NT == alpha_height_NT):
                    alpha_close_NT = i + 1
                    DEBUG(debug_12, f"alpha_close_NT = {alpha_close_NT}")
                    DEBUG(debug_12, f"string_ST[:alpha_close_NT + 1] = {string_ST[:alpha_close_NT + 1]}")
                    not_closed_BL = False                  
                i += 1
                if (i >= len(string_ST)):
                    not_closed_BL = False
                    DEBUG(debug_7, f"L307. alpha_variable_ST = {alpha_variable_ST}")
                    DEBUG(debug_7, f"L308. alpha_open_NT = {alpha_open_NT}")
                    DEBUG(debug_7, f"L309. string_ST                   = {string_ST}")                    
                    DEBUG(debug_7, f"L310. string_ST[alpha_open_NT : ] = {string_ST[alpha_open_NT : ]}")
            alpha_replacer_ST = chr(random.randrange(65, 91)) + chr(random.randrange(65, 91)) + chr(random.randrange(65, 91))
            for i in range(alpha_open_NT, alpha_close_NT - len(alpha_variable_ST) + 1):        # + 1?
                DEBUG(debug_12, f"L315. i = {i}")
                if (string_ST[i:i + len(alpha_variable_ST)] == alpha_variable_ST):            # ?
                    DEBUG(debug_12, f"L317. {string_ST[i:i + len(alpha_variable_ST)]}")
                    if not string_ST[i + len(alpha_variable_ST)].isalnum():
                        DEBUG(debug_12, f"L319. i = {i}")
                        DEBUG(debug_12, f"L320. string_ST[:i]            = {string_ST[:i]}")
                        if (not string_ST[i - 1].isalnum()) or (string_ST[i - 1] == "λ"):
                            DEBUG(debug_12, "L322. Got here!")
                            string_ST = string_ST[:i] + "@"*len(alpha_variable_ST) + string_ST[(i + len(alpha_variable_ST)):]       # ?
            string_ST = string_ST.replace("@"*len(alpha_variable_ST), alpha_replacer_ST)
            DEBUG(debug_9, f"L325. string_ST                = {string_ST}")
    return string_ST
