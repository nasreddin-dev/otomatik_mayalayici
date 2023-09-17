from gizli_kutuphane import cok_gizli_mayalama_tarifi
import time

# Zamanlayiciya gereken sureyi saniye cinsinden veriniz.
def mayala(zamanlayici):
    cok_gizli_mayalama_tarifi()
    time.sleep(zamanlayici)
    print("Mayalama islemi tamamlandi.")

