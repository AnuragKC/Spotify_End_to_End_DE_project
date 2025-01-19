import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node artist
artist_node1732836278412 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://project-data-engineer-akc/staging/artists.csv"], "recurse": True}, transformation_ctx="artist_node1732836278412")

# Script generated for node album
album_node1732836279776 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://project-data-engineer-akc/staging/albums.csv"], "recurse": True}, transformation_ctx="album_node1732836279776")

# Script generated for node tracks
tracks_node1732836280870 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://project-data-engineer-akc/staging/track.csv"], "recurse": True}, transformation_ctx="tracks_node1732836280870")

# Script generated for node Join album and artist
Joinalbumandartist_node1732836560311 = Join.apply(frame1=artist_node1732836278412, frame2=album_node1732836279776, keys1=["id"], keys2=["artist_id"], transformation_ctx="Joinalbumandartist_node1732836560311")

# Script generated for node Join track and albumartist
Jointrackandalbumartist_node1732837022508 = Join.apply(frame1=tracks_node1732836280870, frame2=Joinalbumandartist_node1732836560311, keys1=["track_id"], keys2=["track_id"], transformation_ctx="Jointrackandalbumartist_node1732837022508")

# Script generated for node Drop Fields
DropFields_node1732837167066 = DropFields.apply(frame=Jointrackandalbumartist_node1732837022508, paths=["`.track_id`", "id"], transformation_ctx="DropFields_node1732837167066")

# Script generated for node Destination
Destination_node1732840217547 = glueContext.write_dynamic_frame.from_options(frame=DropFields_node1732837167066, connection_type="s3", format="glueparquet", connection_options={"path": "s3://project-data-engineer-akc/datawarehouse/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="Destination_node1732840217547")

job.commit()