'use client';
import React from "react";
import ModalResponse from "@/components/projects/scenario/ModalResponse";
import ModalCreateScenario from "@/components/projects/scenario/ModalCreateScenario";


export default function Node({ data, onUpdateTree }: { data: ScenarioResponse, onUpdateTree: () => void }) {
  const hasResponse = !!data.response;

  return (
    <div
      className={`p-3 ml-auto mr-auto bg-blue-400 shadow-md bg-opacity-40 rounded-xl hover:bg-blue-600 hover:bg-opacity-40 ${
        hasResponse ? 'w-auto' : 'w-[200px]'
      }`}
    >
      {hasResponse && <strong className="text-sm">{data.response}</strong>}

      <div className="space-x-2 mt-5">
        <ModalResponse data={data}></ModalResponse>
        <ModalCreateScenario parent_id={data.id} project_id={data.project} onUpdateTree={onUpdateTree}></ModalCreateScenario>
      </div>
    </div>
  );
}