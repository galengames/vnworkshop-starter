#Setting up the flowerboy sprite, do not touch unless you know what you are doing.
layeredimage fboy:
    # size (1017, 1080)
    always:
        "fboy_base"
    always:
        "fboy_shadow"
    group extra:
        attribute blush
        attribute normal null default
    always:
        "fboy_eyes"
    group brows auto prefix "b":
        attribute normal default
    group mouth auto prefix "m":
        attribute normal default
    always:
        "fboy_hair"