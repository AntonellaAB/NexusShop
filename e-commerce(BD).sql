--
-- PostgreSQL database dump
--

\restrict pemCsGUOncuWgoflj3Znxf2Cv0iMZGGw9BPfKLKrfkQoJmZw7Ty4GtW07BD7Nmn

-- Dumped from database version 18.6
-- Dumped by pg_dump version 18.6

-- Started on 2026-09-04 14:22:35

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
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
-- TOC entry 222 (class 1259 OID 49171)
-- Name: perfiles_compradores; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.perfiles_compradores (
    id integer NOT NULL,
    usuario_id integer NOT NULL,
    direccion_envio text,
    telefono character varying(25)
);


ALTER TABLE public.perfiles_compradores OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 49170)
-- Name: perfiles_compradores_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.perfiles_compradores_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.perfiles_compradores_id_seq OWNER TO postgres;

--
-- TOC entry 4945 (class 0 OID 0)
-- Dependencies: 221
-- Name: perfiles_compradores_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.perfiles_compradores_id_seq OWNED BY public.perfiles_compradores.id;


--
-- TOC entry 224 (class 1259 OID 49189)
-- Name: perfiles_vendedores; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.perfiles_vendedores (
    id integer NOT NULL,
    usuario_id integer NOT NULL,
    nombre_tienda character varying(100) NOT NULL,
    ruc_o_nit character varying(50),
    estado_verificacion boolean DEFAULT false
);


ALTER TABLE public.perfiles_vendedores OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 49188)
-- Name: perfiles_vendedores_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.perfiles_vendedores_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.perfiles_vendedores_id_seq OWNER TO postgres;

--
-- TOC entry 4946 (class 0 OID 0)
-- Dependencies: 223
-- Name: perfiles_vendedores_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.perfiles_vendedores_id_seq OWNED BY public.perfiles_vendedores.id;


--
-- TOC entry 220 (class 1259 OID 49154)
-- Name: usuarios; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.usuarios (
    id integer NOT NULL,
    correo character varying(255) NOT NULL,
    contrasena_hash character varying(255) NOT NULL,
    tipo_usuario character varying(20) NOT NULL,
    fecha_creacion timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT usuarios_tipo_usuario_check CHECK (((tipo_usuario)::text = ANY ((ARRAY['comprador'::character varying, 'vendedor'::character varying])::text[])))
);


ALTER TABLE public.usuarios OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 49153)
-- Name: usuarios_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.usuarios_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.usuarios_id_seq OWNER TO postgres;

--
-- TOC entry 4947 (class 0 OID 0)
-- Dependencies: 219
-- Name: usuarios_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.usuarios_id_seq OWNED BY public.usuarios.id;


--
-- TOC entry 4767 (class 2604 OID 49174)
-- Name: perfiles_compradores id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfiles_compradores ALTER COLUMN id SET DEFAULT nextval('public.perfiles_compradores_id_seq'::regclass);


--
-- TOC entry 4768 (class 2604 OID 49192)
-- Name: perfiles_vendedores id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfiles_vendedores ALTER COLUMN id SET DEFAULT nextval('public.perfiles_vendedores_id_seq'::regclass);


--
-- TOC entry 4765 (class 2604 OID 49157)
-- Name: usuarios id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuarios ALTER COLUMN id SET DEFAULT nextval('public.usuarios_id_seq'::regclass);


--
-- TOC entry 4937 (class 0 OID 49171)
-- Dependencies: 222
-- Data for Name: perfiles_compradores; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.perfiles_compradores (id, usuario_id, direccion_envio, telefono) FROM stdin;
\.


--
-- TOC entry 4939 (class 0 OID 49189)
-- Dependencies: 224
-- Data for Name: perfiles_vendedores; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.perfiles_vendedores (id, usuario_id, nombre_tienda, ruc_o_nit, estado_verificacion) FROM stdin;
\.


--
-- TOC entry 4935 (class 0 OID 49154)
-- Dependencies: 220
-- Data for Name: usuarios; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.usuarios (id, correo, contrasena_hash, tipo_usuario, fecha_creacion) FROM stdin;
\.


--
-- TOC entry 4948 (class 0 OID 0)
-- Dependencies: 221
-- Name: perfiles_compradores_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.perfiles_compradores_id_seq', 1, false);


--
-- TOC entry 4949 (class 0 OID 0)
-- Dependencies: 223
-- Name: perfiles_vendedores_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.perfiles_vendedores_id_seq', 1, false);


--
-- TOC entry 4950 (class 0 OID 0)
-- Dependencies: 219
-- Name: usuarios_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.usuarios_id_seq', 1, false);


--
-- TOC entry 4776 (class 2606 OID 49180)
-- Name: perfiles_compradores perfiles_compradores_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfiles_compradores
    ADD CONSTRAINT perfiles_compradores_pkey PRIMARY KEY (id);


--
-- TOC entry 4778 (class 2606 OID 49182)
-- Name: perfiles_compradores perfiles_compradores_usuario_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfiles_compradores
    ADD CONSTRAINT perfiles_compradores_usuario_id_key UNIQUE (usuario_id);


--
-- TOC entry 4780 (class 2606 OID 49198)
-- Name: perfiles_vendedores perfiles_vendedores_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfiles_vendedores
    ADD CONSTRAINT perfiles_vendedores_pkey PRIMARY KEY (id);


--
-- TOC entry 4782 (class 2606 OID 49202)
-- Name: perfiles_vendedores perfiles_vendedores_ruc_o_nit_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfiles_vendedores
    ADD CONSTRAINT perfiles_vendedores_ruc_o_nit_key UNIQUE (ruc_o_nit);


--
-- TOC entry 4784 (class 2606 OID 49200)
-- Name: perfiles_vendedores perfiles_vendedores_usuario_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfiles_vendedores
    ADD CONSTRAINT perfiles_vendedores_usuario_id_key UNIQUE (usuario_id);


--
-- TOC entry 4772 (class 2606 OID 49169)
-- Name: usuarios usuarios_correo_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_correo_key UNIQUE (correo);


--
-- TOC entry 4774 (class 2606 OID 49167)
-- Name: usuarios usuarios_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_pkey PRIMARY KEY (id);


--
-- TOC entry 4785 (class 2606 OID 49183)
-- Name: perfiles_compradores perfiles_compradores_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfiles_compradores
    ADD CONSTRAINT perfiles_compradores_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES public.usuarios(id) ON DELETE CASCADE;


--
-- TOC entry 4786 (class 2606 OID 49203)
-- Name: perfiles_vendedores perfiles_vendedores_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfiles_vendedores
    ADD CONSTRAINT perfiles_vendedores_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES public.usuarios(id) ON DELETE CASCADE;


-- Completed on 2026-09-04 14:22:37

--
-- PostgreSQL database dump complete
--

\unrestrict pemCsGUOncuWgoflj3Znxf2Cv0iMZGGw9BPfKLKrfkQoJmZw7Ty4GtW07BD7Nmn

