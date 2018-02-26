# -*- coding: utf-8 -*-
"""
Created on Wed Aug 09 10:54:27 2017

@author: Andres Medina
"""

"""

==============================================================================================================

                                    IMPORT LIBRARIES SECTION

==============================================================================================================

"""

import editdistance
import re
import time
import jellyfish

"""

==============================================================================================================

                                    CONSTANTS SECTION

==============================================================================================================

"""

punctuation = "[\\\"!#$%&'()*+,-./:;<=>?@[\]^_`{|}~]"
tweet_abreviation = { 
"ab" : "about",
"abt" : "about",
"afaik" : "as far as i know",
"ayfkmwts" : "are you fucking kidding me with this s---?",
"b4" : "before",
"bfn" : "bye for now",
"bgd" : "background",
"bh" : "blockhead",
"br" : "best regards",
"btw" : "by the way",
"c" : "see",
"cd9" : "code 9, parents are around",
"chk" : "check",
"cul8r" : "see you later",
"dam" : "don’t annoy me",
"dd" : "dear daughter",
"df" : "dear fiancé",
"dp" : "used to mean “profile pic”",
"ds" : "dear son",
"dyk" : "did you know, do you know",
"effin" : "fucking",
"eml" : "email",
"ema" : "email address",
"f2f" : "face to face",
"ftf" : "face to face",
"fb" : "facebook",
"ff" : "follow friday",
"ffs" : "for fuck‘s sake",
"fml" : "fuck my life.",
"fotd" : "find of the day",
"ftw" : "for the win, fuck the world",
"fubar" : "fucked up beyond all repair (slang from the us military)",
"fwiw" : "for what it's worth.",
"gmafb" : "give me a fucking break",
"gtfooh" : "get the fuck out of here",
"gts" : "guess the song",
"hagn" : "have a good night",
"hotd" : "headline of the day",
"ht" : "heard through",
"hth" : "hope that helps",
"ic" : "i see",
"icymi" : "in case you missed it, a quick way to apologize for retweeting your own material",
"idk" : "i don't know",
"iirc" : "if i remember correctly",
"imho" : "in my humble opinion.",
"irl" : "in real life",
"iwsn" : "i want sex now",
"jk" : "just kidding, joke",
"jsyk" : "just so you know",
"jv" : "joint venture",
"kk" : "kewl kewl, or ok, got it",
"kyso" : "knock your socks off",
"lhh" : "laugh hella hard (stronger version of lol)",
"lmao" : "laughing my ass off",
"lmk" : "let me know",
"lo" : "little one (child)",
"lol" : "laugh out loud",
"mm" : "music monday",
"mirl" : "meet in real life",
"mrjn" : "marijuana",
"nbd" : "no big deal",
"nct" : "nobody cares, though",
"nfw" : "no fucking way",
"njoy" : "enjoy",
"nsfw" : "not safe for work",
"nts" : "note to self",
"omg" : "oh my god",
"omfg" : "oh my fucking god",
"oomf" : "one of my friends/followers",
"orly" : "oh, really?",
"pix" : "pictures",
"plmk" : "please let me know",
"pnp" : "party and play (drugs and sex)",
"ppl" : "people",
"qotd" : "quote of the day",
"re" : "in reply to, in regards to",
"rlrt" : "real-life re-tweet, a close cousin to oh",
"rt" : "retweet",
"rtfm" : "read the f---ing manual",
"rtq" : "read the question",
"sfw" : "safe for work",
"smdh" : "shaking my damn head, smh, only more so",
"smh" : "shaking my head",
"snafu" : "situation normal, all f---ed up (slang from the us military)",
"srs" : "serious",
"stfu" : "shut the fuck up!",
"stfw" : "search the fucking web!",
"tftf" : "thanks for the follow",
"tftt" : "thanks for this tweet",
"tj" : "tweetjack, or joining a conversation belatedly to contribute to a tangent",
"tl" : "timeline",
"tldr" : "too long, didn’t read",
"tmb" : "tweet me back",
"tt" : "trending topic",
"ty" : "thank you",
"tyia" : "thank you in advance",
"tyt" : "take your time",
"tyvw" : "thank you very much",
"w" : "with",
"we" : "whatever",
"wtv" : "whatever",
"u": "you",
"ur": "your",
"ygtr" : "you got that right",
"ykwim" : "you know what i mean",
"ykyat" : "you know you're addicted to",
"ymmv" : "your mileage may vary",
"yolo" : "you only live once",
"yoyo" : "you're on your own",
"yt" : "youtube",
"yw" : "you're welcome",
"zomg" : "oh my god" 
}
"""


==============================================================================================================

                                    FUNCTION DEFINITION SECTION

==============================================================================================================


------------------------------------------------

            FUNCTIONS SECTION

------------------------------------------------

"""

# Function that determines the better matches for a given word, based on the smallest Levenshtein distance
def edit_dist(word, best_score = 9999999999):
    dict.seek(0)
    for token in dict:
        score = editdistance.eval(word, token.strip())
        if (score < best_score):
            best_match = []
            best_match.append(token.strip())
            best_score = score
        elif(score == best_score):
            best_match.append(token.strip())
    return best_match


# Function that determines the better matches for a given word, based on the soundex value
def Soundex(word, dict):
    word_sound = jellyfish.soundex(word.decode('utf-8'))
    match_candidates = []
    for token in dict:
        if (jellyfish.soundex(token.strip().decode('utf-8')) == word_sound):
            match_candidates.append(token.strip().lower())
    return match_candidates


# Function that determines the better matches based on how likely is a word to appear in a sentence
def Most_Likely(list):
    likely = 0.0
    best_match = "???"
    for word in list:
        word_freq.seek(0)
        for line in word_freq:
            match = re.search("^(" + word.lower() + ")\t(.*)$", line)
            if match:
                w = match.group(1)
                p = float(match.group(2))
                if word.lower() ==w and p > likely:
                    likely = p
                    best_match = w
    return best_match

"""


==============================================================================================================

                                    MAIN PROGRAM SECTION

==============================================================================================================

"""

# Toogles of functionalities of the program
twitter_abrev_toggle = 0                                    # For one, we use the twitter abreviation dictionary
soundex_improv_toggle = 1                                   # For one, we use the soundex algorithm for filtering the edit distance results
most_likely_toggle = 1                                      # For one, we use a dictionary with most likely words to improve the sounde / edit distance results


# Variables used in the program
total_words = 0
total_attempts = 0
acc_ans = 0
recall_ans = 0
line_num = 0
baseline_test = -1                                          # 1: Baseline Test  ;   0: Final algorithm test
baseline_method = -1                                        # 1: Edit Distance  ;   0: Soundex
num_iv_words = 0
num_oov_words = 0
num_no_words = 0


# Open required files for reading
file = open('data/labelled-tweets.txt', 'rb')
ans = open('data/labelled-tokens.txt', 'rb')
dict = open('data/dict.txt', 'rb')
word_freq = open('info/words_frequency.txt', 'rb')
output = open('data/output.txt', 'wb')



# We start by calculating the start time of the program
start = time.time()

# Ask the user if we wants to run the program with the baseline test or the normal one
while baseline_test not in [0,1]:
    baseline_test = int(input("Baseline test? (1: YES ; 0: NO): "))

# Ask the user which baseline test wants to perform (Edit Distance or Soundex)
if baseline_test:
    while baseline_method not in [0,1]:
        baseline_method = int(input("Baseline method? (1: Edit distance ; 0: Soundex): "))

# We check every tweet in the input file
for tweet in file:
    line_num += 1
    print("Processing Tweet #: " + str(line_num))


    # We split the line in tokens and we check word by word if we need to translate it
    for token in tweet.split():
        found = 0
        dict.seek(0)
        predict_word = "???"
        predicted_list = []

        # If the token contains any punctuation, we don't translate it
        if not re.search("^" + punctuation + "+$", token):

            total_words += 1

            # If the token contains any punctuation, we don't translate it
            if re.search(punctuation, token):
                predict_word = str(token)
                output.write(str(token) + "\tNO\t" + predict_word + "\n")
                predicted_list.append(predict_word)
                num_no_words += 1

            # If the word is in the twitter abreviation dictionary, then we translate it based on that information
            elif token in tweet_abreviation.keys() and not baseline_test and twitter_abrev_toggle:
                predict_word = tweet_abreviation[token]
                output.write(str(token) + "\tOOV\t" + predict_word + "\n")
                predicted_list.append(predict_word)
                num_oov_words += 1

            else:
            # Then, we search the word in the dictionary ... if exist, we don't translate it either
                for word in dict:
                    if (token == word.strip()):
                        found = 1
                        predict_word = str(token)
                        output.write(str(token) + "\tIV\t" + predict_word + "\n") 
                        predicted_list.append(predict_word)
                        num_iv_words += 1

            # If we can't find the word in the dictionary, then we search the most similar word by using levenshtein distance
                if not found:
                        if (baseline_test) or (not soundex_improv_toggle and not most_likely_toggle):
                            if (baseline_method):
                                ed = edit_dist(token)
                                predicted_list = ed
                                predict_word = ed[0]
                            else:
                                dict.seek(0)
                                sx = Soundex(token, dict)
                                predicted_list = sx
                                if sx:
                                    predict_word = sx[0]
                        elif not soundex_improv_toggle and most_likely_toggle:
                            ed = edit_dist(token)
                            predicted_list = ed
                            predict_word = Most_Likely(ed)
                        elif soundex_improv_toggle and not most_likely_toggle:
                            ed = edit_dist(token)
                            sx = Soundex(token, ed)
                            predicted_list = sx
                            predict_word = sx[0]
                        else:
                            ed = edit_dist(token)
                            sx = Soundex(token, ed)
                            predicted_list = sx
                            predict_word = Most_Likely(sx)

                        output.write(str(token).lower() + "\tOOV\t" + predict_word + "\n")
                        num_oov_words += 1
            
            total_attempts += len(predicted_list)

            # Evaluates the recall of the method
            ans.seek(0)
            found = 0
            for line in ans:
                if line.split()[0] == str(token).lower() and not found:
                    found = 1
                    if line.split()[2] == predict_word:
                        acc_ans += 1
                    if line.split()[2] in predicted_list:
                        recall_ans += 1


accuracy = round((float(acc_ans- num_no_words)*100/(total_words-num_no_words)),2)
recall = round((float(recall_ans- num_no_words)*100/(total_words-num_no_words)),2)
precision = round((float(acc_ans- num_no_words)*100/(total_attempts-num_no_words)),2)
end = time.time()


# Distinguish between algorithm for the printing layout
if baseline_method:
    algorithm = "Edit Distance"
else:
    algorithm = "Soundex"


# Printing results section
print("\n================================================================================================\n")
print("\tTotal Words:\n\n\t\tIV: %s\t\t\tOOV: %s\t\t\tNO: %s" % (num_iv_words, num_oov_words, num_no_words))
print("\n================================================================================================\n")
print("   I." + algorithm + " Baseline Test - Toogles Configuration\n-------------------------------------------\n") if baseline_test else "   I.Improved Edit Distance Toggles Config\n---------------------------------------\n"
print("\t-Twitter Abreviation:\t\t\t\t\tON") if twitter_abrev_toggle and not baseline_test else "\t-Twitter Abreviation:\t\t\t\t\tOFF"
print("\t-Soundex Improvement:\t\t\t\t\tON") if soundex_improv_toggle and not baseline_test else "\t-Soundex Improvement:\t\t\t\t\tOFF"
print("\t-Most Likely Dictionary:\t\t\t\tON") if most_likely_toggle and not baseline_test else "\t-Most Likely Dictionary:\t\t\t\tOFF"
print("\n================================================================================================\n")
print("   II.Evaluation Metrics\n----------------------------\n\n\t1.Accuracy:\t\t\t\t\t\t%s %% (%s/%s)" % (accuracy, acc_ans - num_no_words, total_words - num_no_words))
print("\t2.Precision:\t\t\t\t\t\t%s %% (%s/%s)" % (precision, acc_ans - num_no_words, total_attempts - num_no_words))
print("\t3.Recall:\t\t\t\t\t\t%s %% (%s/%s)" % (recall, recall_ans - num_no_words, total_words - num_no_words))
print("\t4.Execution Time:\t\t\t\t\t%s seconds" % round(end-start,2))
print("\n================================================================================================\n")



# Finally, we close all the used files
ans.close()
word_freq.close()
file.close()
dict.close()
output.close()