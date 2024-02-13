def verify_update_keys(dict):
    expected_keys = {'nome_fantasia', 'CNAE'}

    if set(dict.keys()) != expected_keys:
        return False
    return True