"use client";

import { useRef } from "react";
import { motion, useScroll, useTransform, useInView, useReducedMotion } from "framer-motion";
import { UsersThree, Brain, Lightning, Globe } from "@phosphor-icons/react";

interface Step {
  number: number;
  icon: React.ReactNode;
  title: string;
  body: string;
}

const steps: Step[] = [
  {
    number: 1,
    icon: <Brain weight="duotone" className="h-6 w-6" />,
    title: "Train your clone",
    body: "Upload documents, chat logs, emails, or connect your knowledge base. Your clone learns your tone, your expertise, your style.",
  },
  {
    number: 2,
    icon: <Lightning weight="duotone" className="h-6 w-6" />,
    title: "Set the mode",
    body: "Choose pedagogy, sales, support, or custom mode. Each mode tunes the clone's behavior — from teaching patiently to closing deals.",
  },
  {
    number: 3,
    icon: <UsersThree weight="duotone" className="h-6 w-6" />,
    title: "Share with your audience",
    body: "Embed it on your site, share a link, or connect it to your email and calendar. Your clone works 24/7 in your own voice.",
  },
  {
    number: 4,
    icon: <Globe weight="duotone" className="h-6 w-6" />,
    title: "Watch it scale",
    body: "Track conversations, see what people ask, refine responses. One clone, infinite conversations — all from a single dashboard.",
  },
];

function StepCard({ step, index }: { step: Step; index: number }) {
  const ref = useRef<HTMLDivElement>(null);
  const isInView = useInView(ref, { once: true, amount: 0.3 });
  const reduce = useReducedMotion();

  return (
    <motion.div
      ref={ref}
      initial={reduce ? false : { opacity: 0, y: 48 }}
      animate={isInView ? { opacity: 1, y: 0 } : { opacity: 0, y: 48 }}
      transition={{
        duration: 0.7,
        delay: index * 0.12,
        ease: [0.16, 1, 0.3, 1],
      }}
      className="group relative flex gap-6 rounded-2xl border border-black/5 bg-white p-8 transition-shadow hover:shadow-lg"
    >
      <div className="flex-shrink-0 flex h-12 w-12 items-center justify-center rounded-xl bg-stone-50 text-stone-800 group-hover:bg-stone-100 transition-colors">
        {step.icon}
      </div>
      <div className="min-w-0">
        <div className="flex items-center gap-3 mb-2">
          <span className="inline-flex h-5 w-5 items-center justify-center rounded-full bg-orange-100 text-[11px] font-bold text-orange-600">
            {step.number}
          </span>
          <h3 className="text-lg font-semibold text-stone-900">{step.title}</h3>
        </div>
        <p className="text-sm text-stone-500 leading-relaxed max-w-[48ch]">{step.body}</p>
      </div>
    </motion.div>
  );
}

export function HowItWorks() {
  const sectionRef = useRef<HTMLElement>(null);
  const { scrollYProgress } = useScroll({
    target: sectionRef,
    offset: ["start end", "end start"],
  });

  const lineHeight = useTransform(scrollYProgress, [0, 0.95], ["0%", "100%"]);
  const reduce = useReducedMotion();

  return (
    <section
      ref={sectionRef}
      className="relative w-full max-w-6xl mx-auto px-6 py-24 sm:py-32"
    >
      {/* Section header */}
      <motion.div
        initial={reduce ? false : { opacity: 0, y: 24 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, amount: 0.5 }}
        transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
        className="mb-16 text-center"
      >
        <p className="text-xs font-semibold uppercase tracking-[0.15em] text-stone-400 mb-4">
          How it works
        </p>
        <h2 className="text-3xl sm:text-4xl font-bold tracking-tight text-stone-900">
          From zero to clone in minutes
        </h2>
        <p className="mt-4 text-base text-stone-500 max-w-xl mx-auto">
          Four steps. No code required. Your AI clone goes live the same day you start.
        </p>
      </motion.div>

      {/* Steps with connecting line */}
      <div className="relative">
        {/* Vertical progress line */}
        <div className="absolute left-[2.35rem] top-4 bottom-4 w-px bg-stone-200 sm:left-[2.35rem] hidden sm:block">
          <motion.div
            className="w-full bg-orange-500 origin-top"
            style={{ height: lineHeight }}
          />
        </div>

        <div className="flex flex-col gap-8 sm:gap-6 relative z-10">
          {steps.map((step, i) => (
            <StepCard key={step.number} step={step} index={i} />
          ))}
        </div>
      </div>
    </section>
  );
}
