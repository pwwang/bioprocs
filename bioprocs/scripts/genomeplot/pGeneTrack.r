library (Gviz)
region = unlist(strsplit({{in.region | quote}}, ':', fixed = T))
chrom  = region[1]
region = unlist(strsplit(region[2], '-', fixed = T))
start  = as.numeric(region[1])
end    = as.numeric(region[2])
geneParams = list(
	genome     = {{args.genome | quote}},
	chromosome = chrom,
	from       = start,
	to         = end,
	name       = {{in.name | quote}},
	trackType  = 'GeneRegionTrack',
	table      = 'refGene',
	track      = 'refGene',
	rstarts    = 'exonStarts',
	rends      = 'exonEnds',
	gene       = "name",
	symbol     = "name2",
	transcript = "name",
	strand     = "strand"
)
geneParams = c(geneParams, {{args.params | Rlist}})
geneTrack  = do.call(UcscTrack, geneParams)
saveRDS (geneTrack, {{out.outfile | quote}})