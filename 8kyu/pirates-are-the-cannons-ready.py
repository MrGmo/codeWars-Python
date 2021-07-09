def cannons_ready(gunners):
    count = 0
    for key, value in gunners.items():
      if value == 'nay':
        count += 1
    return 'Shiver me timbers!' if count > 0 else 'Fire!'