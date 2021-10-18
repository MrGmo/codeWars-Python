def replace_all(obj, find, replace):
  if isinstance(obj, str):
    return obj.replace(find, replace)
  elif isinstance(obj, list):
    return [x if x != find else replace for x in obj]