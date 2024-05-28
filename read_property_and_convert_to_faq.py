import pandas as pd

# Reads a single row of a csv file and converts it to a txt in FAQ format.
def read_csv_and_write_to_txt(csv_file, **kwargs):
  """
  This functions reads a single row of a csv file.

  Converts columns and row(questions and answers) into a txt file (FAQ format).

  Mainly used for AI training with questions/answers

  https://docs.vapi.ai/knowledgebase
  """
  filter_value = kwargs.get("filter_value")
  encoding = kwargs.get("encoding", "utf-8")
  start_column = kwargs.get("start_column")
  filter_by = kwargs.get("filter_by")

  # Read the CSV file
  df = pd.read_csv(csv_file, encoding=encoding)

  filtered_row = df[df[filter_by] == filter_value]
  start_index = df.columns.get_loc(start_column)
  output_file_name = filter_value.replace(" ", "_").lower() + ".txt"
  if filtered_row.empty:
      print(f"No rows found with {start_column} = {filter_value}")
      return
  
  with open(output_file_name, 'w') as file:
    row = filtered_row.iloc[0]

    # Iterate over each column (question) starting from the 'filter_by' to the end
    for column in df.columns[start_index:]:
      question = column
      answer = row[column]

      # Write the question and answer to the file
      file.write(f"Q: {question}\n")
      file.write(f"A: {answer}\n")

      # Separator
      file.write("\n\n")


excel_file = "./community_information_collection.csv"

read_csv_and_write_to_txt(excel_file, filter_value="San Cervantes", encoding="ISO-8859-1", start_column="Is your community hybrid?1", filter_by="Community Name")