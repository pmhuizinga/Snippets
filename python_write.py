# write to compressed zip

df.to_csv('sample.csv.gz', compression='gzip')
os.path.getsize('sample.csv.gz')
