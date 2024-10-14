# import concurrent.futures
# import requests
# import threading
# import time


# thread_local = threading.local()


# def get_session():
#     if not hasattr(thread_local, "session"):
#         thread_local.session = requests.Session()
#     return thread_local.session


# def download_site(url):
#     session = get_session()
#     with session.get(url) as response:
#         print(f"Read {len(response.content)} from {url}")


# def download_all_sites(sites):
#     with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
#         executor.map(download_site, sites)


# if __name__ == "__main__":
#     sites = [
#         "https://www.dinamalar.com",
#         "https://thehindu.com",
#     ] * 80
#     start_time = time.time()
#     download_all_sites(sites)
#     duration = time.time() - start_time
#     print(f"Downloaded {len(sites)} in {duration} seconds")


L=len
K=print
import concurrent.futures,requests as D,threading as E,time as B
import google_auth_oauthlib
from tabnanny import check

A=E.local()
def F():
	if not hasattr(A,'session'):A.session=D.Session()
	return A.session

def G(url):
	A=F()
	with A.get(url)as B:K(f"Read {L(B.content)} from {url}")

def H(sites):
	with concurrent.futures.ThreadPoolExecutor(max_workers=10)as A:A.map(G,sites)
if __name__=='__main__':
	C=['https://www.dinamalar.com','https://thehindu.com']*80;
	I=B.time()
	H(C)
	J=B.time()-I
	
	K(f"Downloaded {L(C)} in {J} seconds")