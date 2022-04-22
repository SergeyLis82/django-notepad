function confirmDelete( item ) {
  if (confirm("Удалить " + item + "?")) {
    return true;
  } else {
    return false;
  }
}