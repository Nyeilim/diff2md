# TODO 如果句子里有两个 $ 会出问题, $abc$ \$abc\$ 均显示花体 \\$abc\\$ 显示正常, ==\$abc== 显示正常
def is_all_ignore(origin, sample):
    return str(origin).lower().replace('"', "").replace('.', "").replace(',', "") \
        .replace("'", "").replace('?', "").replace("-", " ") \
        == str(sample).lower().replace('"', "").replace('.', "").replace(',', "") \
        .replace("'", "").replace('?', "").replace("-", " ")


def is_ignore_case(origin, sample):
    return origin.lower() == sample.lower()


def is_ignore_punctuation(origin, sample):
    return str(origin).replace('"', "").replace('.', "").replace(',', "") \
        .replace("'", "").replace('?', "").replace("-", " ") \
        == str(sample).replace('"', "").replace('.', "").replace(',', "") \
        .replace("'", "").replace('?', "").replace("-", " ")
