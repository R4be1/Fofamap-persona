import sys
def Parameter(para):
    if para in sys.argv:
        para=sys.argv.index(para)
        para=sys.argv[para+1] if len(sys.argv) > para+1 else None
        return para
queries=list()
if "-f" in sys.argv:
    for target in open(Parameter("-f")).readlines():
        if target.strip().replace(".","").isdigit():
            queries.append("ip="+target.strip())
        elif "." in target:
            print(target.strip())
            if target[:4]=="www.":
                queries.append( "domain="+target[4:].strip() )
            else:
                queries.append( "domain="+target.strip() )
        else:
            queries.append("title="+target.strip())
print( "("+"||".join(queries)+")" )
    
