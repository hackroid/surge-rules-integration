import requests
import os

TMP_DIR = "./tmp"
SUB_URL_FILE = "./tmp/sub_url.txt"
SUB_CONF = "./tmp/sub.conf"
FULL_CONF = "./tmp/intel.conf"

RULES_URL_FULL = "https://raw.githubusercontent.com/ConnersHua/Profiles/master/Surge/Surge3.conf"


def file_dl(url):
    try:
        file = requests.get(url)
    except requests.exceptions.RequestException as e:
        print("Request error, url not found, please check your link, exiting...")
        raise SystemExit(e)
    print("visiting {}".format(url))
    return file.content.decode("utf-8")


def rules_dl():
    print("Fetching rules...")
    full_str = file_dl(RULES_URL_FULL).strip("\n").strip("\r") + "\n\n\n"
    where_rule = full_str.find("[Host]")
    return full_str[where_rule:]


def sub_dl(url):
    print("Fetching sub...")
    sub_conf_content = file_dl(url)

    if "<html>" in sub_conf_content:
        raise SystemExit("Route error, page not found, please check your link, exiting...")

    if "[Proxy]" not in sub_conf_content or "[Proxy Group]" not in sub_conf_content:
        raise SystemExit("File parsing error, [Proxy]/[Proxy Group] not found, please check your link, exiting...")

    return sub_conf_content


def sub_url_reader():
    sub_url = ""

    if not os.access(TMP_DIR, os.F_OK):
        print("TMP dir not found, creating...")
        os.makedirs(TMP_DIR)
    else:
        print("TMP dir found")

    if not os.access(SUB_URL_FILE, os.F_OK):
        print("SUB_URL_FILE not found, creating...")
        file = open(SUB_URL_FILE, 'w')
        file.close()
        print("SUB_URL_FILE created at \"{}\"".format(SUB_URL_FILE))
        raise SystemExit("Pls add your sub link to the first line of SUB_FILE, then restart this script.\nExiting...")
    else:
        print("SUB_URL_FILE found")

    if not os.access(SUB_URL_FILE, os.R_OK):
        raise SystemExit("SUB_FILE read error")
    else:
        print("SUB_URL_FILE reading...")

    f = open(SUB_URL_FILE, "r")
    sub_url = sub_url.join(f.readline().strip("\n").strip("\r"))
    if len(sub_url) == 0:
        raise SystemExit("SUB_URL_FILE no content, pls check your file")

    print("SUB_URL_FILE url is: {}".format(sub_url))
    return sub_url


def parse_sub(sub_conf_content: str):
    parse_dict = {
        "[General]": sub_conf_content.find("[General]"),
        "[Replica]": sub_conf_content.find("[Replica]"),
        "[Proxy]": sub_conf_content.find("[Proxy]"),
        "[Proxy Group]": sub_conf_content.find("[Proxy Group]"),
        "[Rule]": sub_conf_content.find("[Rule]"),
        "[Host]": sub_conf_content.find("[Host]"),
        "[URL Rewrite]": sub_conf_content.find("[URL Rewrite]"),
        "[Header Rewrite]": sub_conf_content.find("[Header Rewrite]"),
        "[MITM]": sub_conf_content.find("[MITM]"),
        "[Script]": sub_conf_content.find("[Script]")
    }
    nan = [k for k, v in parse_dict.items() if v == -1]
    for k in nan:
        del parse_dict[k]
    parse_dict = sorted(parse_dict.items(), key=lambda d: d[1])
    ProxyGroup = ""
    Proxy = ""
    for i in range(len(parse_dict)):
        if parse_dict[i][0] == "[Proxy]":
            if i + 1 != len(parse_dict):
                Proxy = sub_conf_content[parse_dict[i][1]:parse_dict[i + 1][1]]
            else:
                Proxy = sub_conf_content[parse_dict[i][1]:]
        if parse_dict[i][0] == "[Proxy Group]":
            if i + 1 != len(parse_dict):
                ProxyGroup = sub_conf_content[parse_dict[i][1]:parse_dict[i + 1][1]]
            else:
                ProxyGroup = sub_conf_content[parse_dict[i][1]:]
    if Proxy == "" or ProxyGroup == "":
        raise SystemExit("SUB_FILE parse error, no [Proxy] or [Proxy Group], exiting...")
    ProxyGroup = ProxyGroup[ProxyGroup.find("select,") + 7:].strip(" ")
    ProxyGroup = ProxyGroup[:ProxyGroup.find("\n")]
    return Proxy.strip("\n"), ProxyGroup.strip("\n")


def main():
    f = open("general.conf", "r")
    General = f.read().strip("\n")
    f.close()

    sub_url = sub_url_reader()
    sub_conf_content = sub_dl(sub_url)
    Proxy, proxy_list = parse_sub(sub_conf_content)

    f = open("proxy_group.conf", "r")
    ProxyGroup = f.read().replace("{%%}", proxy_list)
    f.close()

    f = open("rule.conf", "r")
    Rule = f.read()
    f.close()

    After = rules_dl().strip("\n")

    print("Integrating...")
    Final = "\n\n\n".join([General, Proxy, ProxyGroup, Rule, After]) + "\n"
    open(FULL_CONF, 'w').write(Final)
    print("Done @ {}".format(FULL_CONF))


if __name__ == '__main__':
    main()
