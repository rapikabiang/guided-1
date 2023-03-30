def gajibudi(gajiperjam,jamkerja):
    import locale
    locale.setlocale(locale.LC_ALL, locale.getlocale())
    a = gajiperjam*jamkerja*5
    b = a - a*(14/100)
    c = b - a*(1/10)
    d = c - a*(1/100)
    e = d - a*(25/100)
    f = e*(30/100)
    g = e - f
    print('Pendapatan Budi selama libur musim panas sebelum melakukan pembayaran pajak: ',locale.currency(a,grouping=True))
    print('Pendapatan Budi selama libur musim panas setelah melakukan pembayaran pajak: ',locale.currency(b,grouping=True))
    print('Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris: ',locale.currency(c,grouping=True))
    print('Jumlah uang yang akan Budi habiskan untuk membeli alat tulis: ',locale.currency(d,grouping=True))
    print('Jumlah uang yang akan Budi sedekahkan: ',locale.currency(e,grouping=True))
    print('Jumlah uang yang akan diterima anak yatim: ',locale.currency(f,grouping=True))
    print('Jumlah uang yang akan diterima kaum dhuafa: ',locale.currency(g,grouping=True))
gajibudi(100000,56)
