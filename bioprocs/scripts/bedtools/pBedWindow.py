from diot import Diot
from bioprocs.utils import shell

afile    = {{i.afile | quote}}
bfile    = {{i.bfile | quote}}
outfile  = {{o.outfile | quote}}
params   = {{args.params | repr}}
bedtools = {{args.bedtools | quote}}

bedtools = shell.Shell({'bedtools': bedtools}, subcmd = True, equal = ' ', dash = '-').bedtools

params.a = afile
params.b = bfile
params._stdout = outfile
bedtools.window(**params).run()
