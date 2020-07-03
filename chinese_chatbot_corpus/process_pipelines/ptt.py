import codecs
import os

from config import Config
from language.langconv import *
from util import *
import re



def format_converting(text):
    text = text.replace("\t", "\n")
    text = text.strip().split("\n")


    return text



def format_converting_4_nochinese(text):
    #for no_chinese only 
    text = text.replace(" ", "\n")
    text = text.replace("\t", "\n")
    text = text.strip().split("\n")
    

    return text



# def remove_unreasonable_answers(f_read):
#    for index, text in enumerate(f_read):
#        if "沒有資料" in text:
#            continue
#         if "沒有資料" in text:
#             continue
#     return text

#def remove_duplicate_symbols(text):
   # re.sub(ur"([{}]) ".format(punctuation), "\1", line.decode("utf-8"))


def remove_punctuation(text):
    rule = re.compile(r"[^a-zA-Z0-9\u4e00-\u9fa5]")
    text = rule.sub('',text)
    return text

def only_chinese(text):
    rule = re.compile(r"[^\u4e00-\u9fa5]")
    text = rule.sub('',text)
    return text

def no_chinese(text):
    rule = re.compile(r"[\u4e00-\u9fa5]")
    text = rule.sub(' ',text)
    return text


def noise_processing(text):
    r1 = '[a-zA-Z0-9’!"#$%&\'()*+,-./:：;；|<=>?@，—。?★、…【】《》？“”‘’！[\\]^_`{|}~]+＝，。？！～（）—＋＊＆︿％＄＃＠？'
    text = re.sub(r1, "", text)
    punctuation = """！？｡＂＃＄％＆＇（）＊＋－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘'‛“”„‟…‧﹏"""
    re_punctuation = "[{}] ".format(punctuation)
    text = re.sub(re_punctuation, "", text)
    # text = text.replace(" ", "，")
    # text = text.replace("=，=", "")
    # text = text.replace("XD", "")
    # text = text.replace("zz", "")
    # text = text.replace("ㄌ", "了")
    # text = text.replace("，，", "，")
    # text = text.replace("，，，", " ")
    # text = text.replace("ㄇ", "嗎")
    # text = text.replace("ㄉ", "的")
    # text = text.replace("QQ", "")
    # text = text.replace("0.0", "")
    # text = text.replace("ㄏ", "呵")
    # text = text.replace("ㄘ", "吃")
    return text


def prepocess(raw_corpus_file_name, result_file_name):
    #print(raw_corpus_file_name)
    with open(raw_corpus_file_name, 'r', encoding='UTF-8') as f_read:
        with open(result_file_name, 'w', encoding=Config.encoding) as f_write:
            #lines = []
            for index, line in enumerate(f_read):
                
                if index % 100000 == 0:
                    print(raw_corpus_file_name, index)
                if "沒有資料" in line:
                    continue
                if "Tue" in line:
                    continue
                #line = only_chinese(line)
                line = no_chinese(line)
                text = format_converting_4_nochinese(line)
                #text = re.sub(ur"([{}]) ".format(punctuation), "\1", line.decode("utf-8"))
                
                
              
                lines = [line for line in text if line] 
                
                #text.extend(text)

                #print('\n'.join(line)+ '\n')
            #lines = list(set(lines))
                #f_write.writelines("%s\n" % place for place in text)
                f_write.write('\n'.join(lines) + '\r\n')


def prepocess_test(raw_corpus_file_name, result_file_name):
    #print(raw_corpus_file_name)
    with open(raw_corpus_file_name, 'r', encoding='UTF-8') as f_read:
        with open(result_file_name, 'w', encoding=Config.encoding) as f_write:
            #lines = []
            for index, line in enumerate(f_read):
                
                if index % 100000 == 0:
                    print(raw_corpus_file_name, index)
                if "沒有資料" in line:
                    continue
                if "Tue" in line:
                    continue
                #line = only_chinese(line)
                line = no_chinese(line)
                text = format_converting_4_nochinese(line)
                #text = re.sub(ur"([{}]) ".format(punctuation), "\1", line.decode("utf-8"))
                
                
              
                #lines = [line for line in text if line] 
                
                #text.extend(text)

                #print('\n'.join(line)+ '\n')
            #lines = list(set(lines))
                #f_write.writelines("%s\n" % place for place in text)
                f_write.write('\n'.join(text) + '\r\n')

def process_remove_duplicate_symbols(raw_corpus_file_name, result_file_name):

    with open(raw_corpus_file_name, 'r', encoding='UTF-8') as f_read:
        with open(result_file_name, 'w', encoding=Config.encoding) as f_write:
            lines = [line for index, line in enumerate(f_read)]
            s = set(tuple(lines))
            linelist = [t for t in s] 
                
            f_write.writelines("%s" % place for place in linelist)
    
#     linelist = [line for t in s]            
    
    #
                #print(s[:10])
                
            
            #for line in f_read.readline():
            #    print(line)
    #         '''
    #         for index, line in enumerate(f_read.readlines()):
    #             if index % 100000 == 0:
    #                 print(raw_corpus_file_name, index)
    #             print(index)
    #             if "沒有資料" in line:
    #                 continue
    #             print(line)
    #             line = tradition2simple(line)
    #             print(line)
    #             pair = line.strip().split()
    #             print(pair)
    #         '''

    
    # '''
    # raw_corpus_file = codecs.open(raw_corpus_file_name, encoding=Config.encoding, errors="replace")
    # result_file = codecs.open(result_file_name, "w", encoding=Config.encoding)

    # for index, line in enumerate(raw_corpus_file):
    #     if index % 100000 == 0:
    #         print(raw_corpus_file_name, index)

    #     if "沒有資料" in line:
    #         continue
        
    #     line = tradition2simple(line)
    #     print(line)
    #     pair = line.strip().split()

    #     result_file.write("\t".join(pair) + "\n")

    # raw_corpus_file.close()
    # result_file.close()
    # '''

# def prepocess(raw_corpus_file_name, result_file_name):
#     #print(raw_corpus_file_name)
#     with open(raw_corpus_file_name, 'r', encoding='UTF-8') as f_read:
#         with open(result_file_name, 'w', encoding=Config.encoding) as f_write:

#             newmethod664(f_read, raw_corpus_file_name, f_write)

# def newmethod664(f_read, raw_corpus_file_name, f_write):
#     for index, line in enumerate(f_read):

#         if index % 100000 == 0:
#             print(raw_corpus_file_name, index)
#         if "沒有資料" in line:
#             continue
#         if "Tue" in line:
#             continue


#         line = re.sub('[’"#$%&\'()*+-./:;<=>@★…【】：（《》“”‘’^_`{|}~]+', "", line)



#         line = line.replace("\t", "\n")
#         line = line.replace("\r", "\n")


#         line = line.replace(" ", "，")
#         line = line.replace("=，=", "")
#         line = line.replace("XD", "")
#         line = line.replace("zz", "")
#         line = line.replace("ㄌ", "了")
#         line = line.replace("，，", "，")
#         line = line.replace("，，，", " ")
#         line = line.replace("ㄇ", "嗎")
#         line = line.replace("ㄉ", "的")
#         line = line.replace("QQ", "")
#         line = line.replace("0.0", "")
#         line = line.replace("＠＠", "")
#         line = line.replace("ㄏ", "呵")
#         line = line.replace("ㄘ", "吃")
#         line = line.replace(" ", "，")
#         #line = tradition2simple(line)
#         line = line.strip().split("\n")

#         #print('\n'.join(line)+ '\n')
#         f_write.write('\n'.join(line) + '\n\n')




def simple_processing(text):
    print(text)


def ptt_process_pipeline():
    #print("ptt_process_pipeline")

    raw_corpus_file_name = Config.raw_ptt_corpus_path
    result_file_name = os.path.join(Config.clean_chat_corpus_root, "NoChineseWord.txt")
    prepocess(raw_corpus_file_name, result_file_name)
    # format_refine(result_file_name)


def remove_duplicate_symbols():
    #print("ptt_process_pipeline")

    file_name = Config.raw_no_chinese_file_path
    result_file_name = os.path.join(Config.clean_chat_corpus_root, "NoChineseWord_final.txt")
    process_remove_duplicate_symbols(file_name, result_file_name)


#if __name__ == '__main__':
    #ptt_process_pipeline()
