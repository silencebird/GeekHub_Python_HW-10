PGDMP         1                 v         
   HackerNews    10.1    10.1                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false                       1262    16393 
   HackerNews    DATABASE     �   CREATE DATABASE "HackerNews" WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'English_United States.1252' LC_CTYPE = 'English_United States.1252';
    DROP DATABASE "HackerNews";
             postgres    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
             postgres    false                       0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                  postgres    false    3                        3079    12924    plpgsql 	   EXTENSION     ?   CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;
    DROP EXTENSION plpgsql;
                  false                       0    0    EXTENSION plpgsql    COMMENT     @   COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';
                       false    1            �            1259    16528 
   askstories    TABLE     E  CREATE TABLE askstories (
    id integer NOT NULL,
    by text,
    deleted boolean,
    text text,
    dead boolean,
    parent text,
    descendants integer,
    kids integer[],
    score integer,
    "time" timestamp without time zone,
    title text,
    type text,
    url text,
    parts integer[],
    poll integer
);
    DROP TABLE public.askstories;
       public         postgres    false    3            �            1259    16520 
   jobstories    TABLE     E  CREATE TABLE jobstories (
    id integer NOT NULL,
    by text,
    deleted boolean,
    text text,
    dead boolean,
    parent text,
    descendants integer,
    kids integer[],
    score integer,
    "time" timestamp without time zone,
    title text,
    type text,
    url text,
    parts integer[],
    poll integer
);
    DROP TABLE public.jobstories;
       public         postgres    false    3            �            1259    16544 
   newstories    TABLE     E  CREATE TABLE newstories (
    id integer NOT NULL,
    by text,
    deleted boolean,
    text text,
    dead boolean,
    parent text,
    descendants integer,
    kids integer[],
    score integer,
    "time" timestamp without time zone,
    title text,
    type text,
    url text,
    parts integer[],
    poll integer
);
    DROP TABLE public.newstories;
       public         postgres    false    3            �            1259    16536    showstories    TABLE     F  CREATE TABLE showstories (
    id integer NOT NULL,
    by text,
    deleted boolean,
    text text,
    dead boolean,
    parent text,
    descendants integer,
    kids integer[],
    score integer,
    "time" timestamp without time zone,
    title text,
    type text,
    url text,
    parts integer[],
    poll integer
);
    DROP TABLE public.showstories;
       public         postgres    false    3            �
          0    16528 
   askstories 
   TABLE DATA               �   COPY askstories (id, by, deleted, text, dead, parent, descendants, kids, score, "time", title, type, url, parts, poll) FROM stdin;
    public       postgres    false    197           �
          0    16520 
   jobstories 
   TABLE DATA               �   COPY jobstories (id, by, deleted, text, dead, parent, descendants, kids, score, "time", title, type, url, parts, poll) FROM stdin;
    public       postgres    false    196   =                  0    16544 
   newstories 
   TABLE DATA               �   COPY newstories (id, by, deleted, text, dead, parent, descendants, kids, score, "time", title, type, url, parts, poll) FROM stdin;
    public       postgres    false    199   �       �
          0    16536    showstories 
   TABLE DATA               �   COPY showstories (id, by, deleted, text, dead, parent, descendants, kids, score, "time", title, type, url, parts, poll) FROM stdin;
    public       postgres    false    198   6       
           2606    16535    askstories askstories_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY askstories
    ADD CONSTRAINT askstories_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.askstories DROP CONSTRAINT askstories_pkey;
       public         postgres    false    197            }
           2606    16527    jobstories jobstories_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY jobstories
    ADD CONSTRAINT jobstories_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.jobstories DROP CONSTRAINT jobstories_pkey;
       public         postgres    false    196            �
           2606    16551    newstories newstories_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY newstories
    ADD CONSTRAINT newstories_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.newstories DROP CONSTRAINT newstories_pkey;
       public         postgres    false    199            �
           2606    16543    showstories showstories_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY showstories
    ADD CONSTRAINT showstories_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.showstories DROP CONSTRAINT showstories_pkey;
       public         postgres    false    198            �
      x������ � �      �
   g  x��W�n���M?�^��"L��o�(��W��k�m��%�"7"w�ݕd��}��a��3������9s��i�8sx#X�;<���������K3���(���I4���3�����YӐgˊ	�����kC��;��<�1ך5�Rə9s��ܩ����p�X���!�k0����+'4�Q�8��_x��j����&�f#���Ĺ�����TK��~E>���C�p&��u��e�U\�͠�s��0�h�m�Y��2v�4�n�&�e��.�26����rw���~�%+z��/�O8�bίX;���3���3�C���U��1yԪ���$<Z&�߹�b�T��v�/��r�NW�v�����c_k���QӔ@��d��g.���~�	��t%�朼{����g�=;��W.��Ca2s�<uÀ{n�%c7��0�<�t��.�F!\�0Y-�<�p�h<�R�ez��W���︾I�Ϝ�p!�����:Ԑ'�������aR�nZ����?��$Oz�Ϣ pO����X�}��Ε���kfY0p��(�LZr����C�O�p��^a�V���̎�~����n�r9EV��s��3�Zf��}|���h�����"W
���w/�J�L�����ZIn�n�+�`0Y�jf�@�!D7l��՝B��4�<�t�i������Mzy� �f�/����z5�8�����]��ow�Ų'�@�K�$��o�s�ߙ=2'^;��pޑ�Њ�(����+�MO�"�V`IIL��'�̒�\�+f��+<-�i���jf7x����/_E�c�z���tR Tm������Q�8�L���멈�c͌�Ѐ3��j4��LǠ�8]?IA�i�������K���<�=�C�e����� ����G!�c����-k��׌
�֮�����7{�[8�Vxp�Pz���z1�Q��偆��d��cV��pD���@�w���hLW�N��)�����5��7��0̷u�"q^Y~�FǪ�S�+�̹k+��+�T�
�� �K[��Udm͛)�� ��������F�f�H5}_&W:����Wn���l䇩31Lm�q{��j�V�YE|��lkK^%z�n��_��U{h��x��-0��f�Q�V��(Ib�t]���R_�3�;B���0[c-�;u�3(�~�3��D &��8_�䁡�m���ܠ�0��@�jh9kO{Z���L��:�/@�W��D����#:���!AMA�V��(*�ޑ�9�c�^����E�ڶM��0�����LK���r0
�͜'ޢ1|T��NWE)L�ּ	Ƀ�g,�BH���W���7a������d���H�Q]3��wn�Y>*ӟ�0G(��oX��@8��m;���i��3k�`q�4�m���Ee��/`Pz���^:��Rc�o^��G���1��D{`%_W��"���ƞr�[.�/<G�y����`��Y�ɡp}|�H@�QT��߯���(.Y宇�lH��e�,p� 
�F?�M�Y���Sj�~���m"Usְ�>mĿ�f�&no�v{��3��vǿ?�$	�BǊրV�nwx����u%�n݂խ�82m���Ӭ*��?�/~�!h�.���)��;� )E%,��ͦ`�K��Mw���-p�AhS�x�B���3P����	R��|���
X5��HJPe@�
SLp�uw3�9B+�1�0ǵVI����8 �_nB�3Yj^v�h{�F�漻R� �0���fI@�/;?�+�=����m!	�͍��9)��H#�-�����o��֒,��1�&W�72�jz���/?Nv��2i�u�Ab�fXԿρ�"���-���o���󳒥�7/;�cprr�}5'          r  x���A��0��ʯ�[/ul9��6��Miɡ����B����V��5Bq~}�x�M���3���<^�*�Oqp�8HRn�Ğ~��l�8�3��d<�9dE�gMY��S�m[�{$	[���m�A�vn"��`Z {M�����䆑)��o�4Ƹ�z��Z�>��ғAk'�D,����_��n?{'4�Ńz�]��Be�"�$��Xd��%۫v�7毂�;�g�l�'�+bTc��حw���z��;ͦb?��O<GiL��������k}�AQ�+�ƈ�t/���zʲ�9��EY5/��6�9�����&�w�)���]��`t�ة���4�χ���y����(�EJ�d��S��h����i�Z��I��      �
      x������ � �     