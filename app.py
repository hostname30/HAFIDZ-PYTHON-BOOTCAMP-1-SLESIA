from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def kalkulator():
    hasil_akhir = None
    total_harga = None
    besar_diskon = None
    
    if request.method == 'POST':
        try:
            total_harga = float(request.form['total_harga'])
            diskon_persen = float(request.form['diskon'])
            
            # Hitung diskon
            besar_diskon = total_harga * (diskon_persen / 100)
            hasil_akhir = total_harga - besar_diskon
            
            # Format angka pake titik ribuan biar rapi
            total_harga = f"{int(total_harga):,}"
            besar_diskon = f"{int(besar_diskon):,}"
            hasil_akhir = f"{int(hasil_akhir):,}"
        except ValueError:
            pass

    return render_template('index.html', 
                           hasil_akhir=hasil_akhir, 
                           total_harga=total_harga, 
                           besar_diskon=besar_diskon)

if __name__ == '__main__':
    app.run(debug=True)