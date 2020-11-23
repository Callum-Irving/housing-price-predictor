import os
import data_fetcher
import convert_to_csv
import plot
import trainer

data_dir = "data"
data_filename = "houses"

data_path = data_dir + "/" + data_filename
# data_fetcher.fetch(data_path + ".json")
convert_to_csv.to_csv(data_path + ".json", data_path + ".csv")
plot.plot_price_vs_size(data_path + ".csv")
trainer.train(data_path + ".csv", 1)

# TODO measure test set