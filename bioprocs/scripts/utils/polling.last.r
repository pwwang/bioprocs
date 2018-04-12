if (!exists('pollingLast')) {
	pollingLast = function (workdir, length, jobid, cmd, flagfname, t = 10) {
		errorfname = paste(flagfname, '.error', sep='')
		flagfile   = file.path (workdir, jobid, 'output', flagfname)
		errorfile  = file.path (workdir, jobid, 'output', errorfname)
		
		tryCatch ({
			runcmd (cmd)
			file.create (flagfile)
		}, error = function(cond) {
			file.create (errorfile)
			q(save = "no", status = 1)
		})

		if (jobid < length - 1) return ()
		
		wait = T
		while (wait) {
			wait = FALSE
			for (i in 0:(length-1)) {
				efile = file.path (workdir, i, 'output', errorfname)
				ffile = file.path (workdir, i, 'output', flagfname)
				
				if (file.exists(efile)) {
					stop (paste('Job', i, 'failed, I am also exiting ...'), stderr())
				}
				if (!file.exists(ffile)) {
					write (paste('file not exists:', ffile), stderr())
					wait = TRUE
					break
				}
			}
			if (wait) {
				write(paste('Waiting till all other jobs (job # <', length - 1 ,') done ...'), stderr())
				Sys.sleep(t)
			} else {
				break
			}
		}
		
	}
}