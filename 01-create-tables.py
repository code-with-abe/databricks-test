# Databricks notebook source
# MAGIC %md
# MAGIC test notebook

# COMMAND ----------

df = spark.read.option("header","true").csv(get_uc_mount_target('/mnt/raw', normalize=True) + "/uploadpickup.csv")
display(df)
