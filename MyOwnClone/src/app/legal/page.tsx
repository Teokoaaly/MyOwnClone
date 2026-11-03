import type { Metadata } from "next";
import type { ReactNode } from "react";
import AnimatedLogoMark from "@/components/ui/AnimatedLogoMark";
import { Link } from "@/i18n/navigation";

export const metadata: Metadata = {
  title: "Aviso legal | MyOwnClone",
  description: "Aviso legal y condiciones de uso de MyOwnClone.",
};

export default function LegalPage() {
  return (
    <main className="min-h-screen bg-[var(--bg-page)] px-4 py-6 md:px-8 md:py-8">
      <section className="mx-auto flex min-h-[calc(100vh-4rem)] w-full max-w-5xl flex-col rounded-2xl border border-[var(--border-soft)] bg-white p-6 shadow-[0_18px_60px_rgba(15,23,42,0.06)] md:p-10">
        <nav className="flex items-center justify-between border-b border-[var(--border-soft)] pb-5">
          <Link href="/" className="inline-flex items-center gap-2 font-semibold">
            <AnimatedLogoMark size={22} />
            <span>MyOwnClone</span>
          </Link>
          <Link href="/" className="btn-secondary text-xs">
            Volver
          </Link>
        </nav>

        <article className="mt-10 max-w-3xl space-y-8">
          <header>
            <p className="section-label mb-2">Información legal</p>
            <h1 className="text-3xl font-semibold text-[var(--text-primary)]">
              Aviso Legal
            </h1>
            <p className="mt-3 text-sm leading-6 text-[var(--text-secondary)]">
              Última actualización: <time dateTime="2026-05-11">11 de mayo de 2026</time>
            </p>
          </header>

          <LegalBlock title="I. Datos identificativos">
            <p>
              En cumplimiento del deber de información previsto en el artículo 10 de
              la Ley 34/2002 de Servicios de la Sociedad de la Información y de
              Comercio Electrónico (LSSI-CE), le comunicamos que el presente sitio
              web{" "}
              <a className="legal-link" href="https://myownclone.com/">
                myownclone.com
              </a>{" "}
              y sus subdominios (en adelante, el «Sitio Web» o «Myownclone») son
              titularidad de:
            </p>
            <dl className="grid gap-3 rounded-xl bg-slate-50 p-5 sm:grid-cols-[180px_1fr]">
              <dt className="font-medium text-slate-900">Denominación social</dt>
              <dd>Myownclone llc</dd>
              <dt className="font-medium text-slate-900">Tipo de entidad</dt>
              <dd>Limited Liability Company (Wyoming, EE.UU.)</dd>
              <dt className="font-medium text-slate-900">Domicilio registrado</dt>
              <dd>30 N Gould St, Ste R, Sheridan, WY 82801, Estados Unidos</dd>
              <dt className="font-medium text-slate-900">Contacto general</dt>
              <dd>
                <a className="legal-link" href="mailto:contacto@myownclone.com">
                  contacto@myownclone.com
                </a>
              </dd>
              <dt className="font-medium text-slate-900">Protección de datos</dt>
              <dd>
                <a className="legal-link" href="mailto:privacy@myownclone.com">
                  privacy@myownclone.com
                </a>
              </dd>
              <dt className="font-medium text-slate-900">Actividad</dt>
              <dd>
                Plataforma SaaS de clones de inteligencia artificial para creadores
                con marca personal
              </dd>
              <dt className="font-medium text-slate-900">Representantes legales</dt>
              <dd>Jacinto Guzman</dd>
            </dl>
          </LegalBlock>

          <LegalBlock title="II. Objeto del Sitio Web">
            <p>
              Myownclone es una plataforma multi-tenant que permite a creadores con
              marca personal diseñar, entrenar y desplegar un clon de inteligencia
              artificial entrenado sobre su contenido. Cada clon está organizado en
              tres modos de comportamiento (pedagogía, ventas y soporte) y puede
              integrarse tanto dentro de Myownclone como en sitios externos del
              creador.
            </p>
            <p>
              El acceso al panel de administración del creador requiere una
              suscripción activa. Los visitantes que interactúan con un clon
              publicado pueden hacerlo de forma anónima o identificándose mediante
              un código de un solo uso (OTP) enviado a su email.
            </p>
          </LegalBlock>

          <LegalBlock title="III. Hosting y prestadores de servicio">
            <p>
              El Sitio Web está alojado en Vercel Inc. (440 N Barranca Ave #4133,
              Covina, CA 91723, EE.UU.). La base de datos está operada por Neon Inc.
              La lista completa de subencargados del tratamiento se publica en la
              Política de Privacidad.
            </p>
          </LegalBlock>

          <LegalBlock title="IV. Aceptación de las condiciones">
            <p>
              El acceso y uso del Sitio Web atribuye la condición de usuario e
              implica la aceptación plena y sin reservas de las disposiciones
              incluidas en este Aviso Legal, así como en la Política de Privacidad,
              la Política de Cookies y los Términos del Servicio.
            </p>
          </LegalBlock>

          <LegalBlock title="V. Propiedad intelectual e industrial">
            <p>
              Todos los elementos que componen el Sitio Web, incluyendo sin
              limitación el código fuente, diseño, textos, gráficos, logotipos,
              iconos, software y nombres comerciales propios de Myownclone, son
              propiedad de Myownclone llc o de sus respectivos licenciantes y están
              protegidos por las leyes de propiedad intelectual e industrial
              aplicables.
            </p>
            <p>
              El contenido que cada creador (cliente Myownclone) sube a la plataforma
              (textos, vídeos, audios, documentos, conversaciones con su clon)
              permanece en todo momento de su titularidad. Myownclone recibe
              únicamente una licencia limitada, no exclusiva, mundial y libre de
              regalías para procesar dicho contenido con el único fin de prestar el
              servicio contratado. Esta licencia se extingue automáticamente con la
              cancelación de la suscripción del creador, conforme a la política de
              retención descrita en la Política de Privacidad.
            </p>
            <p>
              La marca «Myownclone» es una marca de Myownclone llc. Queda prohibida
              cualquier reproducción no autorizada.
            </p>
          </LegalBlock>

          <LegalBlock title="VI. Responsabilidad del usuario">
            <p>El usuario se compromete a:</p>
            <ul className="list-disc space-y-2 pl-5">
              <li>
                Hacer un uso adecuado del Sitio Web conforme a la ley, la moral y el
                orden público.
              </li>
              <li>
                No utilizar el Sitio Web con fines ilícitos, fraudulentos o
                contrarios a este Aviso Legal.
              </li>
              <li>
                No compartir credenciales de acceso al panel del creador con
                terceros. Cada cuenta es personal e intransferible.
              </li>
              <li>
                No utilizar la plataforma para suplantar la identidad de terceros,
                generar deepfakes no autorizados o entrenar clones a partir de
                contenido sobre el que no se ostentan derechos.
              </li>
              <li>
                No intentar acceder a datos de otros tenants, vulnerar las barreras
                de aislamiento multi-tenant ni realizar ingeniería inversa sobre el
                servicio.
              </li>
            </ul>
          </LegalBlock>

          <LegalBlock title="VII. Naturaleza generativa del servicio">
            <p>
              Myownclone proporciona una capa de inteligencia artificial generativa.
              Las respuestas producidas por un clon se generan automáticamente,
              pueden contener imprecisiones, errores o afirmaciones inexactas y no
              sustituyen el criterio profesional del creador titular del clon, ni
              constituyen asesoramiento jurídico, financiero, médico ni profesional
              de ningún tipo. En cumplimiento del artículo 50 del Reglamento (UE)
              2024/1689 de Inteligencia Artificial, todas las interfaces
              conversacionales de Myownclone identifican explícitamente al
              interlocutor como un clon de IA y no como una persona real.
            </p>
          </LegalBlock>

          <LegalBlock title="VIII. Limitación de responsabilidad">
            <p>
              Myownclone llc no se hace responsable de los daños y perjuicios de
              cualquier naturaleza derivados de la falta de disponibilidad o
              continuidad del Sitio Web, errores en los contenidos o presencia de
              virus u otros componentes dañinos. El servicio se ofrece «tal cual»
              sin SLA contractual durante la fase MVP, comprometiendo únicamente
              esfuerzos razonables de continuidad.
            </p>
          </LegalBlock>

          <LegalBlock title="IX. Modificaciones">
            <p>
              Myownclone llc se reserva el derecho a modificar unilateralmente, en
              cualquier momento, la presentación, configuración y contenidos del
              Sitio Web, así como las condiciones de acceso y uso, notificando los
              cambios sustanciales por email o mediante aviso visible en la
              plataforma.
            </p>
          </LegalBlock>

          <LegalBlock title="X. Legislación aplicable y jurisdicción">
            <p>
              Las presentes condiciones se rigen por la legislación del Estado de
              Wyoming, Estados Unidos, sin perjuicio de las normas imperativas de
              protección al consumidor aplicables en el país de residencia del
              usuario, incluyendo el Reglamento General de Protección de Datos
              (RGPD) y la Ley Orgánica 3/2018 de Protección de Datos Personales y
              garantía de los derechos digitales (LOPDGDD) para residentes en España
              y la Unión Europea.
            </p>
            <p>
              Los consumidores de la Unión Europea podrán dirigir sus reclamaciones
              a la plataforma de resolución de litigios en línea de la Comisión
              Europea:{" "}
              <a
                className="legal-link"
                href="https://ec.europa.eu/consumers/odr"
                rel="noreferrer"
                target="_blank"
              >
                ec.europa.eu/consumers/odr
              </a>
              .
            </p>
          </LegalBlock>
        </article>
      </section>
    </main>
  );
}

function LegalBlock({
  title,
  children,
}: {
  title: string;
  children: ReactNode;
}) {
  return (
    <section className="border-t border-[var(--border-soft)] pt-6">
      <h2 className="text-base font-semibold text-[var(--text-primary)]">
        {title}
      </h2>
      <div className="mt-3 space-y-3 text-sm leading-6 text-[var(--text-secondary)] [&_.legal-link]:font-medium [&_.legal-link]:text-blue-600 [&_.legal-link]:hover:underline">
        {children}
      </div>
    </section>
  );
}
