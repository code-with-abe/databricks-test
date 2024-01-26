# Databricks notebook source
# MAGIC %md
# MAGIC test notebook

# COMMAND ----------

df = spark.read.option("header","true").csv("/mnt/raw/uploadpickup.csv")
display(df)
