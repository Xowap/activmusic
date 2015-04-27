# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
#
# activmusic
# (c) 2014 ActivKonnect

PIPELINE_COMPILERS = (
    'pylesswrap.pipeline_compiler.PyLessWrapCompiler',
)

PIPELINE_CSS = {
    'bootstrap': {
        'source_filenames': (
            'activmusic/bootstrap/bootstrap.less',
        ),
        'output_filename': 'css/bootstrap.css',
    },
}
