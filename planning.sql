--
-- PostgreSQL database dump
--

-- Dumped from database version 11.5 (Ubuntu 11.5-1.pgdg16.04+1)
-- Dumped by pg_dump version 11.5 (Ubuntu 11.5-1.pgdg16.04+1)

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

SET default_with_oids = false;

--
-- Name: conference; Type: TABLE; Schema: public; Owner: thomas
--

CREATE TABLE public.conference (
    id integer NOT NULL,
    title character varying(250) NOT NULL,
    summary text NOT NULL,
    event_date date NOT NULL,
    registering_date timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    event_time time without time zone NOT NULL,
    speaker_id integer
);


ALTER TABLE public.conference OWNER TO thomas;

--
-- Name: conference_id_seq; Type: SEQUENCE; Schema: public; Owner: thomas
--

CREATE SEQUENCE public.conference_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.conference_id_seq OWNER TO thomas;

--
-- Name: conference_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: thomas
--

ALTER SEQUENCE public.conference_id_seq OWNED BY public.conference.id;


--
-- Name: speaker; Type: TABLE; Schema: public; Owner: thomas
--

CREATE TABLE public.speaker (
    id integer NOT NULL,
    firstname character varying(50) NOT NULL,
    lastname character varying(50) NOT NULL,
    job character varying(100) NOT NULL,
    description text,
    is_active boolean DEFAULT true
);


ALTER TABLE public.speaker OWNER TO thomas;

--
-- Name: speaker_id_seq; Type: SEQUENCE; Schema: public; Owner: thomas
--

CREATE SEQUENCE public.speaker_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.speaker_id_seq OWNER TO thomas;

--
-- Name: speaker_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: thomas
--

ALTER SEQUENCE public.speaker_id_seq OWNED BY public.speaker.id;


--
-- Name: conference id; Type: DEFAULT; Schema: public; Owner: thomas
--

ALTER TABLE ONLY public.conference ALTER COLUMN id SET DEFAULT nextval('public.conference_id_seq'::regclass);


--
-- Name: speaker id; Type: DEFAULT; Schema: public; Owner: thomas
--

ALTER TABLE ONLY public.speaker ALTER COLUMN id SET DEFAULT nextval('public.speaker_id_seq'::regclass);


--
-- Data for Name: conference; Type: TABLE DATA; Schema: public; Owner: thomas
--

COPY public.conference (id, title, summary, event_date, registering_date, event_time, speaker_id) FROM stdin;
3	La poo en python	approche et pratiques de la programation orientée objet en python	2019-04-12	2019-09-16 14:21:16.49103	09:15:00	1
5	Le codage ça déménage !	Apprendre le codage en une semaine avec Pole Emploi	2020-05-23	2019-09-16 14:26:25.826233	09:00:00	1
\.


--
-- Data for Name: speaker; Type: TABLE DATA; Schema: public; Owner: thomas
--

COPY public.speaker (id, firstname, lastname, job, description, is_active) FROM stdin;
1	thomas	gossart	formateur	un bon gars	t
9	samantha	rimbert	gestionnaire	femme fonctionnaire de 25 ans	t
\.


--
-- Name: conference_id_seq; Type: SEQUENCE SET; Schema: public; Owner: thomas
--

SELECT pg_catalog.setval('public.conference_id_seq', 12, true);


--
-- Name: speaker_id_seq; Type: SEQUENCE SET; Schema: public; Owner: thomas
--

SELECT pg_catalog.setval('public.speaker_id_seq', 11, true);


--
-- Name: conference conference_pkey; Type: CONSTRAINT; Schema: public; Owner: thomas
--

ALTER TABLE ONLY public.conference
    ADD CONSTRAINT conference_pkey PRIMARY KEY (id);


--
-- Name: speaker speaker_pkey; Type: CONSTRAINT; Schema: public; Owner: thomas
--

ALTER TABLE ONLY public.speaker
    ADD CONSTRAINT speaker_pkey PRIMARY KEY (id);


--
-- Name: conference conference_speaker_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: thomas
--

ALTER TABLE ONLY public.conference
    ADD CONSTRAINT conference_speaker_id_fkey FOREIGN KEY (speaker_id) REFERENCES public.speaker(id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

