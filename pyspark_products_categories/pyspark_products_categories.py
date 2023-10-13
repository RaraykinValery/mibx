from pyspark.sql import SparkSession, Row

spark = SparkSession.builder.getOrCreate()

products = spark.createDataFrame(
    [
        Row(product_id=1, product_name="product_1"),
        Row(product_id=2, product_name="product_2"),
        Row(product_id=3, product_name="product_3"),
    ]
)

categories = spark.createDataFrame(
    [
        Row(category_id=1, category_name="category_1"),
        Row(category_id=2, category_name="category_2"),
        Row(category_id=3, category_name="category_3"),
    ]
)

product_category_relation = spark.createDataFrame(
    [
        Row(product_id=1, category_id=1),
        Row(product_id=1, category_id=3),
        Row(product_id=2, category_id=1),
        Row(product_id=2, category_id=2),
    ]
)

result = (
    products.join(product_category_relation, "product_id", "left")
    .join(categories, "category_id", "left")
    .select(
        products["product_name"].alias("Product"),
        categories["category_name"].alias("Category"),
    )
)

result.show()
