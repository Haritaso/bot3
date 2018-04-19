from mastodon import Mastodon
import re
import operator
def login():
    mastodon = Mastodon(
        client_id = "app_key.txt",
        access_token= "user_key.txt",
        api_base_url= "https://knzk.me"
    )
    return mastodon

def main():
    toots_num = 1200
    mastodon = login()
    toots = []
    next_id = ''
    con = re.compile(r"<[^>]*?>")
    while (len(toots) < toots_num):
        #timelineをn件取得
        timeline = mastodon.timeline(
            timeline = "local",
            limit = "80",
            max_id = next_id
        )
        #新しいトゥートが無ければ終了
        if len(timeline) > 0:
            toots += timeline
        else:
            break
        
        #80件以上のトゥート取得の為のページネーション（？
        toots_last = len(toots)-1
        if toots[toots_last]['_pagination_next']['max_id'] is not None:
            next_id = toots[toots_last]['_pagination_next']['max_id']
        else:
            break
        
        max_len = toots_num if toots_num <len(toots) else len(toots)
        
        
        #整形
        for i in range(0, max_len):      
            toots = sorted(toots, key=lambda x:-x['favourites_count'])
            fav = toots[i]['favourites_count']
            toot_text = str(con.sub('',toots[i]['content']))
            ii = i+1
            print("{}:{}:{}".format(
                ii,
                "Fav数"+str(fav),
                toot_text
                )
            )
            if ii == 10:
                break
if __name__ == '__main__':
    main()
