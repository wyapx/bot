import re

from help import userhelp
from interwikilist import iwlink, iwlist
from .ruserlib import rUser1
from .userlib import User1


async def Username(name):
    name = re.sub(r'^User', 'user', name)
    if name.find(" -h") != -1:
        return (await userhelp())
    elif name.find(" -r") != -1:
        m = re.sub(r' -r', '', name)
        try:
            q = re.match(r'^user-(.*?) (.*)', m)
            w = q.group(1)
            if w in iwlist():
                url = iwlink(w)
                return (await rUser1(url, q.group(2)))
            else:
                return ('未知语言，请使用~user -h查看帮助。')
        except:
            q = re.match(r'^user (.*)', m)
            try:
                s = re.match(r'~(.*?) (.*)', q.group(1))
                metaurl = 'https://' + s.group(1) + '.gamepedia.com/'
                return (await rUser1(metaurl, s.group(2)))
            except:
                try:
                    i = re.match(r'(.*?):(.*)', q.group(1))
                    w = i.group(1)
                    x = i.group(2)
                    if w in iwlist():
                        try:
                            metaurl = iwlink(w)
                            return (await rUser1(metaurl, x))
                        except  Exception as e:
                            return ('发生错误：' + str(e))
                    else:
                        try:
                            metaurl = 'https://minecraft.gamepedia.com/'
                            return (rUser1(metaurl, x))
                        except  Exception as e:
                            return ('发生错误：' + str(e))
                except Exception:
                    metaurl = 'https://minecraft.gamepedia.com/'
                    return (await rUser1(metaurl, q.group(1)))
    else:
        try:
            q = re.match(r'^user-(.*?) (.*)', name)
            w = q.group(1)
            if w in iwlist():
                url = iwlink(w)
                return (await User1(url, q.group(2)))
            else:
                return ('未知语言，请使用~user -h查看帮助。')
        except:
            q = re.match(r'^user (.*)', name)
            try:
                s = re.match(r'~(.*?) (.*)', q.group(1))
                metaurl = 'https://' + s.group(1) + '.gamepedia.com/'
                return (await User1(metaurl, s.group(2)))
            except:
                try:
                    i = re.match(r'(.*?):(.*)', q.group(1))
                    w = i.group(1)
                    x = i.group(2)
                    if w in iwlist():
                        try:
                            metaurl = iwlink(w)
                            return (await User1(metaurl, x))
                        except  Exception as e:
                            return ('发生错误：' + str(e))
                    else:
                        try:
                            metaurl = 'https://minecraft.gamepedia.com/'
                            return (await User1(metaurl, x))
                        except  Exception as e:
                            return ('发生错误：' + str(e))
                except Exception:
                    metaurl = 'https://minecraft.gamepedia.com/'
                    return (await User1(metaurl, q.group(1)))
