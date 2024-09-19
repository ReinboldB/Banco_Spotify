--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0
-- Dumped by pg_dump version 16.0

-- Started on 2024-09-17 15:36:09

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 218 (class 1259 OID 16749)
-- Name: album; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.album (
    id integer NOT NULL,
    duracao time without time zone,
    lancamento date NOT NULL,
    nome character varying NOT NULL
);


ALTER TABLE public.album OWNER TO postgres;

--
-- TOC entry 227 (class 1259 OID 16839)
-- Name: album_compositor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.album_compositor (
    id_album integer NOT NULL,
    id_compositor integer NOT NULL
);


ALTER TABLE public.album_compositor OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16748)
-- Name: album_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.album_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.album_id_seq OWNER TO postgres;

--
-- TOC entry 4881 (class 0 OID 0)
-- Dependencies: 217
-- Name: album_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.album_id_seq OWNED BY public.album.id;


--
-- TOC entry 220 (class 1259 OID 16756)
-- Name: compositor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.compositor (
    id integer NOT NULL,
    nome character varying NOT NULL,
    local_nascimento character varying,
    data_nascimento date
);


ALTER TABLE public.compositor OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16755)
-- Name: compositor_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.compositor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.compositor_id_seq OWNER TO postgres;

--
-- TOC entry 4882 (class 0 OID 0)
-- Dependencies: 219
-- Name: compositor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.compositor_id_seq OWNED BY public.compositor.id;


--
-- TOC entry 222 (class 1259 OID 16765)
-- Name: genero; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.genero (
    id integer NOT NULL,
    nome character varying NOT NULL
);


ALTER TABLE public.genero OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16764)
-- Name: genero_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.genero_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.genero_id_seq OWNER TO postgres;

--
-- TOC entry 4883 (class 0 OID 0)
-- Dependencies: 221
-- Name: genero_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.genero_id_seq OWNED BY public.genero.id;


--
-- TOC entry 216 (class 1259 OID 16740)
-- Name: musica; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.musica (
    id integer NOT NULL,
    nome character varying NOT NULL,
    duracao time without time zone NOT NULL,
    data_criacao date NOT NULL
);


ALTER TABLE public.musica OWNER TO postgres;

--
-- TOC entry 230 (class 1259 OID 16884)
-- Name: musica_album; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.musica_album (
    id_musica integer NOT NULL,
    id_album integer NOT NULL
);


ALTER TABLE public.musica_album OWNER TO postgres;

--
-- TOC entry 229 (class 1259 OID 16869)
-- Name: musica_compositor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.musica_compositor (
    id_musica integer NOT NULL,
    id_compositor integer NOT NULL
);


ALTER TABLE public.musica_compositor OWNER TO postgres;

--
-- TOC entry 228 (class 1259 OID 16854)
-- Name: musica_genero; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.musica_genero (
    id_musica integer NOT NULL,
    id_genero integer NOT NULL
);


ALTER TABLE public.musica_genero OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 16739)
-- Name: musica_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.musica_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.musica_id_seq OWNER TO postgres;

--
-- TOC entry 4884 (class 0 OID 0)
-- Dependencies: 215
-- Name: musica_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.musica_id_seq OWNED BY public.musica.id;


--
-- TOC entry 224 (class 1259 OID 16774)
-- Name: playlist; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.playlist (
    id integer NOT NULL,
    ordem integer NOT NULL,
    nome character varying NOT NULL,
    data_criacao date NOT NULL,
    tempo_total time without time zone NOT NULL
);


ALTER TABLE public.playlist OWNER TO postgres;

--
-- TOC entry 226 (class 1259 OID 16824)
-- Name: playlist_album; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.playlist_album (
    id_playlist integer NOT NULL,
    ordem_playlist integer NOT NULL,
    id_album integer NOT NULL
);


ALTER TABLE public.playlist_album OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 16773)
-- Name: playlist_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.playlist_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.playlist_id_seq OWNER TO postgres;

--
-- TOC entry 4885 (class 0 OID 0)
-- Dependencies: 223
-- Name: playlist_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.playlist_id_seq OWNED BY public.playlist.id;


--
-- TOC entry 225 (class 1259 OID 16809)
-- Name: playlist_musica; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.playlist_musica (
    id_playlist integer NOT NULL,
    ordem_playlist integer NOT NULL,
    id_musica integer NOT NULL
);


ALTER TABLE public.playlist_musica OWNER TO postgres;

--
-- TOC entry 4679 (class 2604 OID 16752)
-- Name: album id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.album ALTER COLUMN id SET DEFAULT nextval('public.album_id_seq'::regclass);


--
-- TOC entry 4680 (class 2604 OID 16759)
-- Name: compositor id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.compositor ALTER COLUMN id SET DEFAULT nextval('public.compositor_id_seq'::regclass);


--
-- TOC entry 4681 (class 2604 OID 16768)
-- Name: genero id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.genero ALTER COLUMN id SET DEFAULT nextval('public.genero_id_seq'::regclass);


--
-- TOC entry 4678 (class 2604 OID 16743)
-- Name: musica id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.musica ALTER COLUMN id SET DEFAULT nextval('public.musica_id_seq'::regclass);


--
-- TOC entry 4682 (class 2604 OID 16777)
-- Name: playlist id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.playlist ALTER COLUMN id SET DEFAULT nextval('public.playlist_id_seq'::regclass);


--
-- TOC entry 4863 (class 0 OID 16749)
-- Dependencies: 218
-- Data for Name: album; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.album (id, duracao, lancamento, nome) FROM stdin;
\.


--
-- TOC entry 4872 (class 0 OID 16839)
-- Dependencies: 227
-- Data for Name: album_compositor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.album_compositor (id_album, id_compositor) FROM stdin;
\.


--
-- TOC entry 4865 (class 0 OID 16756)
-- Dependencies: 220
-- Data for Name: compositor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.compositor (id, nome, local_nascimento, data_nascimento) FROM stdin;
\.


--
-- TOC entry 4867 (class 0 OID 16765)
-- Dependencies: 222
-- Data for Name: genero; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.genero (id, nome) FROM stdin;
1	popp
3	rocky
\.


--
-- TOC entry 4861 (class 0 OID 16740)
-- Dependencies: 216
-- Data for Name: musica; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.musica (id, nome, duracao, data_criacao) FROM stdin;
3	Morango	01:00:00	2020-01-01
\.


--
-- TOC entry 4875 (class 0 OID 16884)
-- Dependencies: 230
-- Data for Name: musica_album; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.musica_album (id_musica, id_album) FROM stdin;
\.


--
-- TOC entry 4874 (class 0 OID 16869)
-- Dependencies: 229
-- Data for Name: musica_compositor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.musica_compositor (id_musica, id_compositor) FROM stdin;
\.


--
-- TOC entry 4873 (class 0 OID 16854)
-- Dependencies: 228
-- Data for Name: musica_genero; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.musica_genero (id_musica, id_genero) FROM stdin;
\.


--
-- TOC entry 4869 (class 0 OID 16774)
-- Dependencies: 224
-- Data for Name: playlist; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.playlist (id, ordem, nome, data_criacao, tempo_total) FROM stdin;
\.


--
-- TOC entry 4871 (class 0 OID 16824)
-- Dependencies: 226
-- Data for Name: playlist_album; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.playlist_album (id_playlist, ordem_playlist, id_album) FROM stdin;
\.


--
-- TOC entry 4870 (class 0 OID 16809)
-- Dependencies: 225
-- Data for Name: playlist_musica; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.playlist_musica (id_playlist, ordem_playlist, id_musica) FROM stdin;
\.


--
-- TOC entry 4886 (class 0 OID 0)
-- Dependencies: 217
-- Name: album_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.album_id_seq', 1, false);


--
-- TOC entry 4887 (class 0 OID 0)
-- Dependencies: 219
-- Name: compositor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.compositor_id_seq', 1, false);


--
-- TOC entry 4888 (class 0 OID 0)
-- Dependencies: 221
-- Name: genero_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.genero_id_seq', 4, true);


--
-- TOC entry 4889 (class 0 OID 0)
-- Dependencies: 215
-- Name: musica_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.musica_id_seq', 3, true);


--
-- TOC entry 4890 (class 0 OID 0)
-- Dependencies: 223
-- Name: playlist_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.playlist_id_seq', 1, false);


--
-- TOC entry 4698 (class 2606 OID 16843)
-- Name: album_compositor album_compositor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.album_compositor
    ADD CONSTRAINT album_compositor_pkey PRIMARY KEY (id_album, id_compositor);


--
-- TOC entry 4686 (class 2606 OID 16754)
-- Name: album album_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.album
    ADD CONSTRAINT album_pkey PRIMARY KEY (id);


--
-- TOC entry 4688 (class 2606 OID 16763)
-- Name: compositor compositor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.compositor
    ADD CONSTRAINT compositor_pkey PRIMARY KEY (id);


--
-- TOC entry 4690 (class 2606 OID 16772)
-- Name: genero genero_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.genero
    ADD CONSTRAINT genero_pkey PRIMARY KEY (id);


--
-- TOC entry 4704 (class 2606 OID 16888)
-- Name: musica_album musica_album_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.musica_album
    ADD CONSTRAINT musica_album_pkey PRIMARY KEY (id_musica, id_album);


--
-- TOC entry 4702 (class 2606 OID 16873)
-- Name: musica_compositor musica_compositor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.musica_compositor
    ADD CONSTRAINT musica_compositor_pkey PRIMARY KEY (id_musica, id_compositor);


--
-- TOC entry 4700 (class 2606 OID 16858)
-- Name: musica_genero musica_genero_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.musica_genero
    ADD CONSTRAINT musica_genero_pkey PRIMARY KEY (id_musica, id_genero);


--
-- TOC entry 4684 (class 2606 OID 16747)
-- Name: musica musica_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.musica
    ADD CONSTRAINT musica_pkey PRIMARY KEY (id);


--
-- TOC entry 4696 (class 2606 OID 16828)
-- Name: playlist_album playlist_album_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.playlist_album
    ADD CONSTRAINT playlist_album_pkey PRIMARY KEY (id_playlist, ordem_playlist, id_album);


--
-- TOC entry 4694 (class 2606 OID 16813)
-- Name: playlist_musica playlist_musica_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.playlist_musica
    ADD CONSTRAINT playlist_musica_pkey PRIMARY KEY (id_playlist, ordem_playlist, id_musica);


--
-- TOC entry 4692 (class 2606 OID 16781)
-- Name: playlist playlist_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.playlist
    ADD CONSTRAINT playlist_pkey PRIMARY KEY (id, ordem);


--
-- TOC entry 4707 (class 2606 OID 16834)
-- Name: playlist_album id_album; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.playlist_album
    ADD CONSTRAINT id_album FOREIGN KEY (id_album) REFERENCES public.album(id) NOT VALID;


--
-- TOC entry 4709 (class 2606 OID 16844)
-- Name: album_compositor id_album; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.album_compositor
    ADD CONSTRAINT id_album FOREIGN KEY (id_album) REFERENCES public.album(id) NOT VALID;


--
-- TOC entry 4715 (class 2606 OID 16894)
-- Name: musica_album id_album; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.musica_album
    ADD CONSTRAINT id_album FOREIGN KEY (id_album) REFERENCES public.album(id) NOT VALID;


--
-- TOC entry 4710 (class 2606 OID 16849)
-- Name: album_compositor id_compositor; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.album_compositor
    ADD CONSTRAINT id_compositor FOREIGN KEY (id_compositor) REFERENCES public.compositor(id) NOT VALID;


--
-- TOC entry 4713 (class 2606 OID 16879)
-- Name: musica_compositor id_compositor; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.musica_compositor
    ADD CONSTRAINT id_compositor FOREIGN KEY (id_compositor) REFERENCES public.compositor(id) NOT VALID;


--
-- TOC entry 4711 (class 2606 OID 16864)
-- Name: musica_genero id_genero; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.musica_genero
    ADD CONSTRAINT id_genero FOREIGN KEY (id_genero) REFERENCES public.genero(id) NOT VALID;


--
-- TOC entry 4705 (class 2606 OID 16819)
-- Name: playlist_musica id_musica; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.playlist_musica
    ADD CONSTRAINT id_musica FOREIGN KEY (id_musica) REFERENCES public.musica(id) NOT VALID;


--
-- TOC entry 4712 (class 2606 OID 16859)
-- Name: musica_genero id_musica; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.musica_genero
    ADD CONSTRAINT id_musica FOREIGN KEY (id_musica) REFERENCES public.musica(id) NOT VALID;


--
-- TOC entry 4714 (class 2606 OID 16874)
-- Name: musica_compositor id_musica; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.musica_compositor
    ADD CONSTRAINT id_musica FOREIGN KEY (id_musica) REFERENCES public.musica(id) NOT VALID;


--
-- TOC entry 4716 (class 2606 OID 16889)
-- Name: musica_album id_musica; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.musica_album
    ADD CONSTRAINT id_musica FOREIGN KEY (id_musica) REFERENCES public.musica(id) NOT VALID;


--
-- TOC entry 4706 (class 2606 OID 16814)
-- Name: playlist_musica id_playlist; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.playlist_musica
    ADD CONSTRAINT id_playlist FOREIGN KEY (id_playlist, ordem_playlist) REFERENCES public.playlist(id, ordem) NOT VALID;


--
-- TOC entry 4708 (class 2606 OID 16829)
-- Name: playlist_album id_playlist; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.playlist_album
    ADD CONSTRAINT id_playlist FOREIGN KEY (id_playlist, ordem_playlist) REFERENCES public.playlist(id, ordem) NOT VALID;


-- Completed on 2024-09-17 15:36:10

--
-- PostgreSQL database dump complete
--

