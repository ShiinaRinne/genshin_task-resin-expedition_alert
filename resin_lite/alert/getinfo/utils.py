def get_server(uid: int) -> str:
    if str(uid).startswith('1'):
        return 'cn_gf01'  # 天空岛
    elif str(uid).startswith('5'):
        return 'cn_qd01'  # 世界树
    else:
        return ''
