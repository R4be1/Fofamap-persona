queries_file = open("queries.txt","w")
for A in range(1,255):
    for B in range(0,256):
        queries_file.write(f'is_domain=true && title!="404 Not Found" && status_code="200" && ip="{A}.{B}.0.0/16"'+"\n")
queries_file.close()
