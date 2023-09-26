from sch_day.sakhaday import sakha_day
from sch_pres.sakhapress import sakha_press
from sch_news.sakhanews import sakha_news



def main():
    #https://sakhaday.ru/
    sakha_d = sakha_day()
    if 'Error' in sakha_d :
        print(sakha_d)
        post_text1 = sakha_d
    else:
        sakha_day_title = sakha_d[0]
        sakha_day_text = sakha_d[1]
        post_text = f'*{sakha_day_title}* \n\n {sakha_day_text}'
        if len(post_text) < 4095:
                post_text1 = post_text
        else:
            print('Error41 - большой текст с сайта sakha_day')
            post_text1 = 'Error41 - большой текст с сайта sakha_day'


    # https://sakhapress.ru/
    sakha_pr = sakha_press()
    if 'Error' in sakha_pr:
        print(sakha_pr)
        post_text2 = sakha_pr
    else:
        sakha_press_title = sakha_pr[0]
        sakha_press_text = sakha_pr[1]
        post_text = f'*{sakha_press_title}* \n\n {sakha_press_text}'
        if len(post_text) < 4095:
                post_text2 = post_text
        else:
            print('Error42 - большой текст с сайта sakha_press')
            post_text2 = 'Error42 - большой текст с сайта sakha_press'

        
        
    # https://1sn.ru/
    sakha_n = sakha_news()
    if 'Error' in sakha_n:
        print(sakha_n)
        post_text3 = sakha_n
    else:
        sakha_news_title = sakha_n[0]
        sakha_news_text = sakha_n[1]
        post_text = f'*{sakha_news_title}* \n\n {sakha_news_text}'
        if len(post_text) < 4095:
                post_text3 = post_text
        else:
            print('Error43 - большой текст с сайта sakha_news')
            post_text3 = 'Error43 - большой текст с сайта sakha_news'

    return post_text1,post_text2,post_text3
        
    



