
# // tag::imports[]
from graphframes import *
from pyspark import SparkContext, SQLContext
# // end::imports[]

# // tag::sqlcontext[]
sqlContext = SQLContext(sc)
# // end::sqlcontext[]

# // tag::load-graph-frame[]
v = sqlContext.read.csv("data/social-nodes.csv", header=True)
e = sqlContext.read.csv("data/social-relationships.csv", header=True)
g = GraphFrame(v, e)
# // end::load-graph-frame[]

# // tag::degree[]
total_degree = g.degrees
in_degree = g.inDegrees
out_degree = g.outDegrees

total_degree.join(in_degree, "id", how="left") \
            .join(out_degree, "id", how="left") \
            .fillna(0) \
            .sort("inDegree", ascending=False) \
            .show()
# // end::degree[]