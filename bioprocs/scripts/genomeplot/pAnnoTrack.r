library (Gviz)
region = unlist(strsplit({{in.chrom | quote}}, ':', fixed = T))
chrom  = region[1]
params = list(
	range      = {{in.infile | quote}},
	genome     = {{args.genome | quote}},
	chromosome = chrom,
	name       = {{in.name | quote}}
)
params = c(params, {{args.params | Rlist}})
track  = do.call(AnnotationTrack, params)
saveRDS (track, {{out.outfile | quote}})