"use client";

import { useState } from "react";
import styles from "../page.module.css";

type DemoTab = "inbox" | "memory" | "dashboard";

const labels: Readonly<Record<DemoTab, string>> = { inbox: "Triaje de buzón y ventas", memory: "Biblioteca y memoria", dashboard: "Panel en tiempo real" };

export function CloneSimulator() {
  const [activeTab, setActiveTab] = useState<DemoTab>("inbox");
  const [queryCount, setQueryCount] = useState(3);
  return <div className={styles.simulator}>
    <div className={styles.tabs} role="tablist" aria-label="Capacidades del clon">{(Object.keys(labels) as DemoTab[]).map((tab) => <button aria-selected={activeTab === tab} className={activeTab === tab ? styles.tabActive : styles.tab} key={tab} onClick={() => setActiveTab(tab)} role="tab" type="button">{labels[tab]}</button>)}</div>
    {activeTab === "inbox" && <div className={styles.workspaceGrid} role="tabpanel"><article><div className={styles.panelHeader}>Consultas entrantes ({queryCount})</div><button className={styles.simulate} onClick={() => setQueryCount((count) => count + 1)} type="button">+ Simular email</button><p><b>Intención de venta</b><br />¿Ofrecen acceso a API y soporte dedicado?</p><p><b>Consulta de producto</b><br />¿Cuánto tarda el entrenamiento del clon?</p></article><article><div className={styles.panelHeader}>Clon IA generando respuesta</div><p className={styles.tone}>Tono: profesional y directo</p><blockquote>“Sí, el plan Enterprise incluye acceso completo a API, integraciones personalizadas y soporte dedicado.”</blockquote><span>Respuesta lista para revisar</span></article><article><div className={styles.panelHeader}>Actividad automatizada 24/7</div><p><b>Producto recomendado</b><br />Plan Pro sugerido a un cliente potencial.</p><p><b>FAQ resuelta</b><br />Preguntas sobre integración contestadas.</p><span>Flujo activo</span></article></div>}
    {activeTab === "memory" && <div className={styles.memoryPanel} role="tabpanel"><h3>Biblioteca y memoria listas para responder</h3><div><p><b>Documentos subidos</b><br />PDF, web y contenido de negocio indexados.</p><p><b>Memorias de creador</b><br />Voz, tono y reglas del clon calibradas.</p><p><b>Conocimiento verificable</b><br />Respuestas conectadas con tu propia fuente.</p></div></div>}
    {activeTab === "dashboard" && <div className={styles.memoryPanel} role="tabpanel"><h3>Actividad y métricas del clon</h3><div><p><b>Triaje y respuesta automática</b><br />Conectado al espacio de trabajo del equipo.</p><p><b>Chat público</b><br />Un enlace compartible para atender consultas.</p><p><b>Visibilidad operativa</b><br />Todo el contexto, en un mismo panel.</p></div></div>}
  </div>;
}
