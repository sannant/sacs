
def select_parameters(df, fixed_parameters):
    selection = df["id"] != ""
    for k, v in fixed_parameters.items():
        try:
            for ki, vi in v.items():
                selection &= df[k+'.'+ki] == vi
        except AttributeError:
            selection &= df[k] == v
    return selection