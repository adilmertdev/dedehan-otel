import json, html, os
BASE="https://adilmertdev.github.io/dedehan-otel/"
TEL="+904627113661"; TEL_TXT="0462 711 36 61"
GSM="+905464650161"; GSM_TXT="0546 465 01 61"; WA="905464650161"
ADDR="Yeşiltepe Mah. Mehmet Akif Ersoy Cad. No:93, 61900 Arsin / Trabzon"
LAT,LNG=40.953379,39.935476
MAPQ="Dedehan Otel, Mehmet Akif Ersoy Cd. No:93, 61900 Arsin/Trabzon"
I={ # icons
'wifi':'<path d="M5 12.55a11 11 0 0 1 14.08 0M1.42 9a16 16 0 0 1 21.16 0M8.53 16.11a6 6 0 0 1 6.95 0M12 20h.01"/>',
'car':'<path d="M5 17h14M6 17v2M18 17v2M3 13l2-6a2 2 0 0 1 2-1.4h10A2 2 0 0 1 19 7l2 6v4H3z"/><circle cx="7.5" cy="13.5" r=".5"/><circle cx="16.5" cy="13.5" r=".5"/>',
'clock':'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
'coffee':'<path d="M17 8h1a4 4 0 0 1 0 8h-1M3 8h14v9a4 4 0 0 1-4 4H7a4 4 0 0 1-4-4z"/><path d="M6 2v2M10 2v2M14 2v2"/>',
'bell':'<path d="M3 18h18M5 18a7 7 0 0 1 14 0M12 8V6M10 6h4"/>',
'plane':'<path d="M17.8 19.2 16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5l-.3.5c-.2.5-.1 1 .3 1.3L9 12l-2 3H4l-1 1 3 2 2 3 1-1v-3l3-2 3.5 5.3c.3.4.8.5 1.3.3l.5-.2c.4-.3.6-.7.5-1.2z"/>',
'lift':'<rect x="5" y="2" width="14" height="20" rx="2"/><path d="m9 8 3-3 3 3M9 16l3 3 3-3"/>',
'safe':'<rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="12" cy="12" r="3"/><path d="M12 9v1M12 14v1M3 20v1M21 20v1"/>',
'snow':'<path d="M12 2v20M4.9 4.9l14.2 14.2M2 12h20M4.9 19.1 19.1 4.9"/>',
'tv':'<rect x="2" y="6" width="20" height="13" rx="2"/><path d="m17 2-5 4-5-4"/>',
'shirt':'<path d="M20.4 6.6 16 3c-.8 1.2-2.3 2-4 2s-3.2-.8-4-2L3.6 6.6 6 10l2-1v12h8V9l2 1z"/>',
'bag':'<rect x="4" y="7" width="16" height="14" rx="2"/><path d="M9 7V4a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v3"/>',
'sun':'<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
'map':'<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
'phone':'<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
'users':'<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>',
'size':'<path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/>',
'mtn':'<path d="m8 3 4 8 5-5 5 15H2z"/>',
'check':'<path d="M20 6 9 17l-5-5"/>',
'cert':'<circle cx="12" cy="8" r="6"/><path d="M15.5 13 17 22l-5-3-5 3 1.5-9"/>',
'sea':'<path d="M2 6c.6.5 1.2 1 2.5 1C7 7 7 5 9.5 5c2.6 0 2.4 2 5 2 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1M2 12c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 2.6 0 2.4 2 5 2 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1M2 18c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 2.6 0 2.4 2 5 2 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1"/>',
}
def ic(n): return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{I[n]}</svg>'
WA_SVG='<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.4-.5c.2-.2.2-.3.3-.5.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.1-.3-.2-.6-.3zM12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.5 0-3-.4-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2z"/></svg>'

T={
'tr':dict(lang='tr',locale='tr_TR',p='',other='en/',
 title='Dedehan Otel | Arsin, Trabzon – Deniz Kenarında Konforlu Konaklama',
 desc="Dedehan Otel, Trabzon Arsin'de 25 klimalı odası, açık büfe kahvaltısı, ücretsiz otoparkı ve 24 saat resepsiyonuyla sizi bekliyor. Trabzon Havalimanı'na 15 km.",
 nav=[('#hakkimizda','Otel'),('#odalar','Odalar'),('#olanaklar','Olanaklar'),('#galeri','Galeri'),('#konum','Konum'),('#iletisim','İletişim')],
 book='Rezervasyon',
 h_eye='Arsin · Trabzon · Karadeniz',h1='Karadeniz’in kıyısında<br><em>evinizdeki rahatlık</em>',
 h_p="Arsin merkezinde, denize birkaç dakika yürüme mesafesinde; tertemiz odalar, zengin kahvaltı ve güler yüzlü bir ekip.",
 h_cta1='WhatsApp ile Rezervasyon',h_cta2='Odaları İncele',
 f1=('25','klimalı oda'),f2='Giriş 14:00 · Çıkış 12:00',f3='Havalimanına ~15 km',f4='Ücretsiz Wi‑Fi & otopark',
 a_eye='Otelimiz',a_h='Arsin’de sıcak bir mola',
 a_p1="Dedehan Otel, Trabzon’un Arsin ilçesinde, Yeşiltepe Mahallesi’nde yer alıyor. İş seyahatinde, aile tatilinde ya da Karadeniz turunuzun bir durağında; şehrin kalabalığından uzak, sakin ama her şeye yakın bir konaklama sunuyoruz.",
 a_p2="Otelimizde 25 klimalı oda, her sabah açık büfe kahvaltı, 24 saat resepsiyon ve oda servisi bulunuyor. Çevrede market, eczane ve restoranlar yürüme mesafesinde.",
 ticks=['Açık büfe kahvaltı (08:00–11:00)','24 saat resepsiyon & oda servisi','Ücretsiz özel otopark','Havalimanı transferi (ücretli)'],
 cert_t='T.C. Kültür ve Turizm Bakanlığı',cert_s='Turizm İşletmesi Belgesi No: 18770',
 r_eye='Odalar',r_h='Size uygun odayı seçin',r_lead='Tüm odalarda klima, minibar, uydu yayınlı LCD TV, ücretsiz Wi‑Fi, emanet kasası, çalışma masası ve duşlu özel banyo bulunur.',
 rooms=[('Standart Çift Kişilik Oda','oda-1','25 m²','3 kişiye kadar','Dağ manzaralı','Tek büyük yataklı, ferah ve sade bir oda. Çiftler ve iş seyahatleri için ideal.'),
        ('Üç Kişilik Oda','oda-2','27 m²','4 kişiye kadar','Dağ manzaralı','Bir büyük ve bir tek kişilik yataklı; küçük aileler ve arkadaş grupları için.'),
        ('Dört Kişilik Oda','oda-calisma','30 m²','5 kişiye kadar','Dağ manzaralı','Bir çift kişilik ve iki tek kişilik yataklı, geniş aile odası.')],
 r_btn='Bu oda için sor',r_note='Güncel fiyat ve müsaitlik için bize WhatsApp veya telefonla ulaşın.',
 m_eye='Olanaklar',m_h='Konforunuz için her detay',m_lead='Konaklamanızı kolaylaştıran hizmetler ve oda olanakları.',
 amen=[('wifi','Ücretsiz Wi‑Fi','Tüm otelde'),('car','Ücretsiz Otopark','Tesis içinde özel'),('coffee','Açık Büfe Kahvaltı','Her gün 08:00–11:00'),('bell','24 Saat Resepsiyon','Oda servisi dahil'),
       ('plane','Havalimanı Transferi','Ücretli, talep üzerine'),('lift','Asansör','Tüm katlara erişim'),('snow','Klima','Tüm odalarda'),('tv','LCD TV','Uydu yayınlı'),
       ('safe','Emanet Kasası','Odalarda'),('shirt','Kuru Temizleme','Çamaşır hizmeti'),('bag','Bagaj Saklama','Giriş/çıkışta'),('sun','Teras & Ortak Salon','Dinlenme alanı')],
 pol=['Giriş: 14:00','Çıkış: 12:00','Kredi kartı geçerlidir'],
 g_eye='Galeri',g_h='Otelden kareler',
 caps={'havadan-deniz':'Otel ve Karadeniz manzarası','dis-cephe-gece':'Otel cephesi – gece','lobi':'Lobi ve resepsiyon','kahvalti':'Kahvaltı salonu','oda-1':'Standart oda','oda-2':'Oda','oda-calisma':'Oda – çalışma alanı','banyo':'Banyo','dus':'Duş','dis-cephe-yan':'Otel cephesi'},
 v_eye='Misafir Yorumları',v_h='Misafirlerimiz ne diyor?',
 sc=[('4,3','Google Haritalar','487 değerlendirme · /5'),('8,4','Booking.com','65 değerlendirme · /10')],
 revs=[('Harika harika harika başka söze gerek yok. Kendinizi evinizde hissedebileceğiniz bölgenin en iyi oteli. İş seyahatleri için ayda en az 1 kere kalıyorum.','Misafir yorumu · haritane.com'),
       ('Temiz, zengin kahvaltı, çözüme odaklı yaklaşım, güler yüz.','Misafir yorumu · haritane.com'),
       ('Odalar klimalı ve güzeldi, kahvaltı çok iyiydi. Konum pratik; yakında market, eczane ve mağazalar var, denize yürüyerek gidilebiliyor.','Google yorumu (İngilizceden çeviri) · Ağustos 2025')],
 l_eye='Konum',l_h='Arsin’in kalbinde',l_lead='Trabzon Havalimanı’na yaklaşık 15 km. Sahile birkaç dakikalık yürüme mesafesindeyiz.',
 near=[('Trabzon Havalimanı (TZX)','15,1 km'),('Trabzon Cevahir Outlet','9 km'),('Kaşüstü Plajı','9,3 km'),('Yalıncak Aile Plajı','11,6 km'),('Atatürk Köşkü','15,6 km'),('Forum Trabzon AVM','17,1 km'),('Kaymaklı Manastırı','~19 km'),('Boztepe Piknik Alanı','~20 km'),('Trabzon Meydan Parkı','20,3 km')],
 l_src='Mesafeler kuş uçuşu yaklaşık değerlerdir.',l_dir='Yol Tarifi Al',
 c_eye='İletişim & Rezervasyon',c_h='Yerinizi ayırtalım',
 c_card='Bize ulaşın',c_addr='Adres',c_tel='Resepsiyon',c_gsm='Cep / WhatsApp',c_hours='Resepsiyon',c_hours_v='7/24 açık',
 c_call='Hemen Ara',c_wa='WhatsApp',
 fm_h='Rezervasyon talebi',fm_lead='Formu doldurun, talebiniz hazır bir WhatsApp mesajı olarak açılsın. Onay için ekibimiz size dönüş yapacaktır.',
 fm=dict(name='Ad Soyad',phone='Telefon (isteğe bağlı)',cin='Giriş tarihi',cout='Çıkış tarihi',guests='Kişi sayısı',room='Oda tipi',note='Not (isteğe bağlı)',any='Fark etmez',send='WhatsApp ile Gönder',
   hi='Merhaba, Dedehan Otel için rezervasyon talebim var.',req='Lütfen ad soyad ve tarihleri doldurun.',dates='Çıkış tarihi giriş tarihinden sonra olmalı.'),
 ft_about='Arsin, Trabzon’da konforlu ve samimi konaklama. Turizm İşletmesi Belgesi No: 18770.',ft_menu='Menü',ft_ct='İletişim',ft_rights='Tüm hakları saklıdır.',ft_lang='English',
 wa_aria='WhatsApp ile yazın',gal_close='Kapat',gal_prev='Önceki',gal_next='Sonraki',menu='Menü'),
'en':dict(lang='en',locale='en_US',p='../',other='../',
 title='Dedehan Hotel | Arsin, Trabzon – Comfortable Stay by the Black Sea',
 desc='Dedehan Hotel in Arsin, Trabzon: 25 air-conditioned rooms, buffet breakfast, free parking and a 24-hour front desk. About 15 km from Trabzon Airport.',
 nav=[('#hakkimizda','Hotel'),('#odalar','Rooms'),('#olanaklar','Amenities'),('#galeri','Gallery'),('#konum','Location'),('#iletisim','Contact')],
 book='Book now',
 h_eye='Arsin · Trabzon · Black Sea',h1='On the Black Sea coast,<br><em>feel right at home</em>',
 h_p='In the centre of Arsin, a few minutes’ walk from the sea: spotless rooms, a generous breakfast and a friendly team.',
 h_cta1='Book via WhatsApp',h_cta2='View Rooms',
 f1=('25','air-conditioned rooms'),f2='Check-in 14:00 · Check-out 12:00',f3='~15 km to the airport',f4='Free Wi‑Fi & parking',
 a_eye='Our Hotel',a_h='A warm stop in Arsin',
 a_p1='Dedehan Hotel is located in the Yeşiltepe neighbourhood of Arsin, Trabzon. Whether you are on a business trip, a family holiday or touring the Black Sea, we offer a calm stay away from the city crowds, yet close to everything.',
 a_p2='The hotel has 25 air-conditioned rooms, a buffet breakfast every morning, a 24-hour front desk and room service. Markets, pharmacies and restaurants are within walking distance.',
 ticks=['Buffet breakfast (08:00–11:00)','24-hour front desk & room service','Free private parking','Airport shuttle (surcharge)'],
 cert_t='Ministry of Culture and Tourism',cert_s='Tourism Operation Certificate No: 18770',
 r_eye='Rooms',r_h='Choose your room',r_lead='All rooms have air conditioning, a minibar, LCD TV with satellite channels, free Wi‑Fi, a safe, a desk and a private bathroom with shower.',
 rooms=[('Standard Double Room','oda-1','25 m²','Up to 3 guests','Mountain view','A bright, simple room with one large bed. Ideal for couples and business travellers.'),
        ('Triple Room','oda-2','27 m²','Up to 4 guests','Mountain view','One large and one single bed; great for small families and friends.'),
        ('Quadruple Room','oda-calisma','30 m²','Up to 5 guests','Mountain view','One double and two single beds – a spacious family room.')],
 r_btn='Ask about this room',r_note='Contact us via WhatsApp or phone for current rates and availability.',
 m_eye='Amenities',m_h='Every detail for your comfort',m_lead='Services and in-room features that make your stay easier.',
 amen=[('wifi','Free Wi‑Fi','Throughout the hotel'),('car','Free Parking','Private, on site'),('coffee','Buffet Breakfast','Daily 08:00–11:00'),('bell','24h Front Desk','Room service included'),
       ('plane','Airport Shuttle','Surcharge, on request'),('lift','Elevator','Access to all floors'),('snow','Air Conditioning','In all rooms'),('tv','LCD TV','Satellite channels'),
       ('safe','In-room Safe','In every room'),('shirt','Dry Cleaning','Laundry service'),('bag','Luggage Storage','At check-in/out'),('sun','Terrace & Lounge','Shared relaxing area')],
 pol=['Check-in: 14:00','Check-out: 12:00','Credit cards accepted'],
 g_eye='Gallery',g_h='Moments from the hotel',
 caps={'havadan-deniz':'The hotel and the Black Sea','dis-cephe-gece':'Hotel façade at night','lobi':'Lobby & reception','kahvalti':'Breakfast hall','oda-1':'Standard room','oda-2':'Room','oda-calisma':'Room – work area','banyo':'Bathroom','dus':'Shower','dis-cephe-yan':'Hotel façade'},
 v_eye='Guest Reviews',v_h='What our guests say',
 sc=[('4.3','Google Maps','487 reviews · /5'),('8.4','Booking.com','65 reviews · /10')],
 revs=[('The staff were very helpful and friendly, the rooms were air conditioned. There are many restaurants and markets near this hotel and Arsin beach is so close — you can reach it in 4 or 5 minutes.','Google review · August 2025'),
       ('The rooms were air-conditioned and good. The breakfast was very good. The location is practical, with markets, a pharmacy and shops nearby, close to the sea to walk.','Google review · August 2025'),
       ('Clean, rich breakfast, solution-oriented approach, smiling faces.','Guest review (translated from Turkish) · haritane.com')],
 l_eye='Location',l_h='In the heart of Arsin',l_lead='About 15 km from Trabzon Airport, and just a few minutes’ walk from the seaside.',
 near=[('Trabzon Airport (TZX)','15.1 km'),('Trabzon Cevahir Outlet','9 km'),('Kaşüstü Beach','9.3 km'),('Yalıncak Family Beach','11.6 km'),('Atatürk Pavilion','15.6 km'),('Forum Trabzon Mall','17.1 km'),('Kaymaklı Monastery','~19 km'),('Boztepe Picnic Area','~20 km'),('Trabzon Meydan Park','20.3 km')],
 l_src='Distances are approximate straight-line values.',l_dir='Get Directions',
 c_eye='Contact & Booking',c_h='Let us reserve your room',
 c_card='Get in touch',c_addr='Address',c_tel='Reception',c_gsm='Mobile / WhatsApp',c_hours='Front desk',c_hours_v='Open 24/7',
 c_call='Call Now',c_wa='WhatsApp',
 fm_h='Booking request',fm_lead='Fill in the form and your request opens as a ready-to-send WhatsApp message. Our team will get back to you to confirm.',
 fm=dict(name='Full name',phone='Phone (optional)',cin='Check-in',cout='Check-out',guests='Guests',room='Room type',note='Note (optional)',any='No preference',send='Send via WhatsApp',
   hi='Hello, I would like to make a booking request at Dedehan Hotel.',req='Please enter your name and dates.',dates='Check-out must be after check-in.'),
 ft_about='Comfortable, friendly accommodation in Arsin, Trabzon. Tourism Operation Certificate No: 18770.',ft_menu='Menu',ft_ct='Contact',ft_rights='All rights reserved.',ft_lang='Türkçe',
 wa_aria='Message us on WhatsApp',gal_close='Close',gal_prev='Previous',gal_next='Next',menu='Menu'),
}
GAL=[('havadan-deniz','w2 h2'),('dis-cephe-gece','h2'),('lobi',''),('kahvalti',''),('oda-1','w2'),('oda-2',''),('oda-calisma','h2'),('banyo',''),('dus',''),('dis-cephe-yan','')]
e=html.escape
def page(k):
    t=T[k];p=t['p']
    url=BASE+('' if k=='tr' else 'en/')
    nav=''.join(f'<a href="{h}">{n}</a>' for h,n in t['nav'])
    tr_on,en_on=('on','') if k=='tr' else ('','on')
    tr_href='./' if k=='tr' else '../'; en_href='en/' if k=='tr' else './'
    rooms=''.join(f'''<article class="room rv d{i}"><div class="room-img"><img src="{p}assets/img/{img}-sm.webp" alt="{e(n)}" loading="lazy" width="720" height="540"></div><div class="room-body"><h3>{n}</h3><div class="room-meta"><span>{ic("size")}{sz}</span><span>{ic("users")}{cap}</span><span>{ic("mtn")}{view}</span></div><p>{d}</p><a class="btn btn-line" href="#iletisim" data-room="{e(n)}">{t["r_btn"]}</a></div></article>''' for i,(n,img,sz,cap,view,d) in enumerate(t['rooms']))
    amen=''.join(f'<div class="am rv d{i%4}">{ic(a)}<b>{b}</b><span>{s}</span></div>' for i,(a,b,s) in enumerate(t['amen']))
    pol=''.join(f'<div>{x}</div>' for x in t['pol'])
    gal=''.join(f'<button class="{c} rv" data-full="{p}assets/img/{n}.webp" data-cap="{e(t["caps"][n])}" aria-label="{e(t["caps"][n])}"><img src="{p}assets/img/{n}-sm.webp" alt="{e(t["caps"][n])}" loading="lazy"><figcaption>{t["caps"][n]}</figcaption></button>' for n,c in GAL)
    sc=''.join(f'<div class="score"><b>{a}</b><span><strong>{b}</strong>{c}</span></div>' for a,b,c in t['sc'])
    revs=''.join(f'<blockquote class="rev rv d{i}"><div class="stars" aria-label="5/5">★★★★★</div><p>{q}</p><small>{s}</small></blockquote>' for i,(q,s) in enumerate(t['revs']))
    near=''.join(f'<li><span>{a}</span><b>{b}</b></li>' for a,b in t['near'])
    fm=t['fm']
    ropts=f'<option>{fm["any"]}</option>'+''.join(f'<option>{r[0]}</option>' for r in t['rooms'])
    gopts=''.join(f'<option{" selected" if g==2 else ""}>{g}</option>' for g in range(1,6))
    ft_js=json.dumps(dict(hi=fm['hi'],name=fm['name'],cin=fm['cin'],cout=fm['cout'],guests=fm['guests'],room=fm['room'],phone=fm['phone'].split(' (')[0],note=fm['note'].split(' (')[0],req=fm['req'],dates=fm['dates']),ensure_ascii=False)
    maps_dir=f'https://www.google.com/maps/dir/?api=1&destination={LAT},{LNG}'
    ld={"@context":"https://schema.org","@type":"Hotel","name":"Dedehan Otel","alternateName":"Dedehan Hotel","url":url,"image":[BASE+"assets/img/havadan-deniz.webp",BASE+"assets/img/dis-cephe-gece.webp"],
        "description":t['desc'],"telephone":TEL,"address":{"@type":"PostalAddress","streetAddress":"Yeşiltepe Mah. Mehmet Akif Ersoy Cad. No:93","addressLocality":"Arsin","addressRegion":"Trabzon","postalCode":"61900","addressCountry":"TR"},
        "geo":{"@type":"GeoCoordinates","latitude":LAT,"longitude":LNG},"checkinTime":"14:00","checkoutTime":"12:00","numberOfRooms":25,
        "amenityFeature":[{"@type":"LocationFeatureSpecification","name":n,"value":True} for n in ["Free WiFi","Free parking","24-hour front desk","Room service","Airport shuttle","Elevator","Air conditioning","Breakfast"]],
        "aggregateRating":{"@type":"AggregateRating","ratingValue":4.3,"bestRating":5,"reviewCount":487}}
    return f'''<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{t['title']}</title>
<meta name="description" content="{e(t['desc'])}">
<meta name="theme-color" content="#0b3b42">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="tr" href="{BASE}">
<link rel="alternate" hreflang="en" href="{BASE}en/">
<link rel="alternate" hreflang="x-default" href="{BASE}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Dedehan Otel">
<meta property="og:title" content="{e(t['title'])}">
<meta property="og:description" content="{e(t['desc'])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}assets/og.jpg">
<meta property="og:locale" content="{t['locale']}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{p}assets/favicon.svg" type="image/svg+xml">
<link rel="icon" href="{p}assets/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="{p}assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500&family=Manrope:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="preload" as="image" href="{p}assets/img/havadan-deniz.webp">
<link rel="stylesheet" href="{p}css/style.css">
<script type="application/ld+json">{json.dumps(ld,ensure_ascii=False)}</script>
</head>
<body>
<header class="hdr"><div class="wrap">
<a class="brand" href="#top"><img src="{p}assets/favicon.svg" alt="" width="40" height="40"><span><b>Dedehan</b><small>{'Otel · Arsin' if k=='tr' else 'Hotel · Arsin'}</small></span></a>
<nav class="nav" aria-label="{t['menu']}">{nav}<span class="lang"><a href="{tr_href}" class="{tr_on}" hreflang="tr" lang="tr">TR</a><a href="{en_href}" class="{en_on}" hreflang="en" lang="en">EN</a></span><a class="btn btn-sand" href="#iletisim">{t['book']}</a></nav>
<button class="burger" aria-label="{t['menu']}" aria-expanded="false"><span></span></button>
</div></header>
<main id="top">
<section class="hero">
<div class="hero-bg"><img src="{p}assets/img/havadan-deniz.webp" alt="{e(t['caps']['havadan-deniz'])}" fetchpriority="high"></div>
<div class="wrap">
<span class="eyebrow rv">{t['h_eye']}</span>
<h1 class="rv d1">{t['h1']}</h1>
<p class="rv d2">{t['h_p']}</p>
<div class="hero-cta rv d3"><a class="btn btn-sand" href="https://wa.me/{WA}" target="_blank" rel="noopener">{WA_SVG}{t['h_cta1']}</a><a class="btn btn-ghost" href="#odalar">{t['h_cta2']}</a></div>
<div class="hero-facts rv d3"><div><b>{t['f1'][0]}</b>{t['f1'][1]}</div><div>{ic('clock')}{t['f2']}</div><div>{ic('plane')}{t['f3']}</div><div>{ic('wifi')}{t['f4']}</div></div>
</div>
</section>

<section id="hakkimizda"><div class="wrap about-grid">
<div class="about-media rv"><img class="a1" src="{p}assets/img/dis-cephe-gece-sm.webp" alt="{e(t['caps']['dis-cephe-gece'])}" loading="lazy"><img class="a2" src="{p}assets/img/lobi-sm.webp" alt="{e(t['caps']['lobi'])}" loading="lazy"><div class="badge-cert">{ic('cert') if False else ''}<b>{t['cert_t']}</b>{t['cert_s']}</div></div>
<div><span class="eyebrow rv">{t['a_eye']}</span><h2 class="rv d1">{t['a_h']}</h2><p class="lead rv d2">{t['a_p1']}</p><p class="lead rv d2" style="margin-top:14px">{t['a_p2']}</p>
<ul class="ticks rv d3">{''.join(f'<li>{ic("check")}{x}</li>' for x in t['ticks'])}</ul>
<a class="btn btn-teal rv d3" href="#iletisim">{t['book']}</a></div>
</div></section>

<section id="odalar" class="rooms"><div class="wrap">
<div class="sec-head"><div><span class="eyebrow rv">{t['r_eye']}</span><h2 class="rv d1">{t['r_h']}</h2><p class="lead rv d2">{t['r_lead']}</p></div></div>
<div class="room-grid">{rooms}</div>
<p class="room-note rv">{t['r_note']}</p>
</div></section>

<section id="olanaklar" class="amen"><div class="wrap">
<span class="eyebrow rv">{t['m_eye']}</span><h2 class="rv d1">{t['m_h']}</h2><p class="lead rv d2">{t['m_lead']}</p>
<div class="amen-grid">{amen}</div>
<div class="policy rv">{pol}</div>
</div></section>

<section id="galeri"><div class="wrap">
<div class="sec-head"><div><span class="eyebrow rv">{t['g_eye']}</span><h2 class="rv d1">{t['g_h']}</h2></div></div>
<div class="gal">{gal}</div>
</div></section>

<section id="yorumlar" class="reviews"><div class="wrap">
<div class="sec-head"><div><span class="eyebrow rv">{t['v_eye']}</span><h2 class="rv d1">{t['v_h']}</h2></div><div class="scores rv d2">{sc}</div></div>
<div class="rev-grid">{revs}</div>
</div></section>

<section id="konum"><div class="wrap loc-grid">
<div><span class="eyebrow rv">{t['l_eye']}</span><h2 class="rv d1">{t['l_h']}</h2><p class="lead rv d2">{t['l_lead']}</p>
<div class="addr rv">{ic('map')}<span>{ADDR}</span></div>
<ul class="near rv">{near}</ul><p class="src">{t['l_src']}</p>
<a class="btn btn-teal" style="margin-top:22px" href="{maps_dir}" target="_blank" rel="noopener">{ic('map')}{t['l_dir']}</a></div>
<div class="map rv d1"><iframe title="Google Maps – Dedehan Otel" src="https://maps.google.com/maps?q={e(MAPQ.replace(' ','+'))}&amp;hl={t['lang']}&amp;z=16&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
</div></section>

<section id="iletisim" class="contact"><div class="wrap">
<span class="eyebrow rv">{t['c_eye']}</span><h2 class="rv d1">{t['c_h']}</h2>
<div class="ct-grid" style="margin-top:30px">
<div class="ct-card rv"><h3>{t['c_card']}</h3>
<div class="ct-item">{ic('map')}<div><small>{t['c_addr']}</small>{ADDR}</div></div>
<div class="ct-item">{ic('phone')}<div><small>{t['c_tel']}</small><a href="tel:{TEL}">{TEL_TXT}</a></div></div>
<div class="ct-item">{ic('phone')}<div><small>{t['c_gsm']}</small><a href="tel:{GSM}">{GSM_TXT}</a></div></div>
<div class="ct-item">{ic('clock')}<div><small>{t['c_hours']}</small>{t['c_hours_v']}</div></div>
<div class="ct-btns"><a class="btn btn-sand" href="tel:{TEL}">{ic('phone')}{t['c_call']}</a><a class="btn btn-wa" href="https://wa.me/{WA}" target="_blank" rel="noopener">{WA_SVG}{t['c_wa']}</a></div>
</div>
<form class="inq rv d1" novalidate data-wa="{WA}" data-t='{e(ft_js)}'>
<h3>{t['fm_h']}</h3><p class="lead">{t['fm_lead']}</p>
<div class="f full"><label for="f-name">{fm['name']}</label><input id="f-name" name="name" autocomplete="name" required></div>
<div class="f"><label for="f-in">{fm['cin']}</label><input id="f-in" name="in" type="date" required></div>
<div class="f"><label for="f-out">{fm['cout']}</label><input id="f-out" name="out" type="date" required></div>
<div class="f"><label for="f-g">{fm['guests']}</label><select id="f-g" name="guests">{gopts}</select></div>
<div class="f"><label for="f-r">{fm['room']}</label><select id="f-r" name="room">{ropts}</select></div>
<div class="f full"><label for="f-p">{fm['phone']}</label><input id="f-p" name="phone" type="tel" autocomplete="tel"></div>
<div class="f full"><label for="f-n">{fm['note']}</label><textarea id="f-n" name="note"></textarea></div>
<p class="form-err" role="alert"></p>
<div class="form-btns"><button class="btn btn-wa" type="submit">{WA_SVG}{fm['send']}</button><a class="btn btn-line" href="tel:{TEL}">{ic('phone')}{t['c_call']}</a></div>
</form>
</div></div></section>
</main>

<footer><div class="wrap">
<div class="ft">
<div><a class="brand" href="#top"><img src="{p}assets/favicon.svg" alt="" width="40" height="40"><span><b>Dedehan</b><small>{'Otel · Arsin' if k=='tr' else 'Hotel · Arsin'}</small></span></a><p style="margin-top:16px;max-width:40ch">{t['ft_about']}</p></div>
<div><h4>{t['ft_menu']}</h4><ul>{''.join(f'<li><a href="{h}">{n}</a></li>' for h,n in t['nav'])}</ul></div>
<div><h4>{t['ft_ct']}</h4><ul><li>{ADDR}</li><li><a href="tel:{TEL}">{TEL_TXT}</a></li><li><a href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp: {GSM_TXT}</a></li><li><a href="{t['other'] if k=='tr' else '../'}" hreflang="{'en' if k=='tr' else 'tr'}">{t['ft_lang']}</a></li></ul></div>
</div>
<div class="ft-bottom"><span>© <span id="yr">2026</span> Dedehan Otel. {t['ft_rights']}</span><span>Arsin · Trabzon</span></div>
</div></footer>

<a class="fab" href="https://wa.me/{WA}" target="_blank" rel="noopener" aria-label="{t['wa_aria']}">{WA_SVG}</a>
<div class="lb" role="dialog" aria-modal="true"><button class="x" aria-label="{t['gal_close']}">✕</button><button class="p" aria-label="{t['gal_prev']}">‹</button><img alt=""><button class="n" aria-label="{t['gal_next']}">›</button><div class="cap"></div></div>
<script src="{p}js/main.js" defer></script>
</body>
</html>'''
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.makedirs(root+'/en',exist_ok=True)
open(root+'/index.html','w').write(page('tr'))
open(root+'/en/index.html','w').write(page('en'))
open(root+'/robots.txt','w').write(f'User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n')
open(root+'/sitemap.xml','w').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{BASE}</loc></url><url><loc>{BASE}en/</loc></url></urlset>\n')
print('built')
