'use client';

import { Edge, Node, ReactFlowProvider } from 'reactflow';

import Flow from '@/components/projects/scenario/Flow';

const initialNodes: Node[] = [
  { id: 'node-1', type: 'childNode', position: { x: 0, y: 0 }, data: { value: 123 } },
  { id: 'node-2', type: 'rootNode', position: { x: 0, y: 0 }, data: { value: 123 } },
];

const initialEdges: Edge[] = [
  { id: 'e1-2', source: '1', target: '2', animated: true },
  { id: 'e1-3', source: '1', target: '3', animated: true },
];


interface PageParams {
	slug: string;
}


export default function Page({params}: { params: PageParams }) {
	const slug = params.slug;

  return (
    <main >
      <h1 className="text-2xl">{slug}</h1>
      <ReactFlowProvider initialNodes={initialNodes} initialEdges={initialEdges}>
        <Flow nodes={initialNodes} edges={initialEdges} />
      </ReactFlowProvider>
    </main>
  );
}