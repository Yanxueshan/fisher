# from flask_cache import Cache
这样使用flask_cache导入Cache时会出错，需要修改以下flask_cache的源码，将flask_cache包下的jinjia2ext模块中的from flask.ext.cache import make_template_fragment_key注释掉，加上from flask_cache import make_template_fragment_key
