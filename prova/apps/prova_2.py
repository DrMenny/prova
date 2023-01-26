data = ['ok - email.pdf', 'ok - Bug_su_it.wikipedia_testo_su_thumb_con_chrome-ConvertImage.tif', 'ok - sentenza.pdf',
        'ok - Fwd_ restituzione degli atti firmati.eml', 'ok - log.txt', 'ok - GNN.jpg', 'ok - example.docx',
        'ok - ezyzip.zip', 'ok - Data_Masking.doc', 'ok - career.png']

for doc in data:
  if doc == "error":
      yield 'error'
else:
    return "ok"