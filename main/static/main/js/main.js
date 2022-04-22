function confirmDelete() {
  if (confirm("Удалить заметку?")) {
    return true;
  } else {
    return false;
  }
}