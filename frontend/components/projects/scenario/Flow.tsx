'use client';

import {useCallback, useMemo, useState} from 'react';
import {ChildNode, RootNode} from './CustomNode';
import ReactFlow, {
	addEdge,
	applyEdgeChanges,
	applyNodeChanges,
	Edge,
	Node,
	OnConnect,
	OnEdgesChange,
	OnNodesChange,
} from 'reactflow';
import 'reactflow/dist/style.css';


export default function App({
															nodes: initNodes,
															edges: initEdges,
														}: {
	nodes: Node[];
	edges: Edge[];
}) {
	const [nodes, setNodes] = useState<Node[]>(initNodes);
	const [edges, setEdges] = useState<Edge[]>(initEdges);
	const nodeTypes = useMemo(() => ({childNode: ChildNode, rootNode: RootNode}), []);

	const onNodesChange: OnNodesChange = useCallback(
		(chs) => {
			setNodes((nds) => applyNodeChanges(chs, nds));
		},
		[setNodes]
	);

	const onEdgesChange: OnEdgesChange = useCallback(
		(chs) => {
			setEdges((eds) => applyEdgeChanges(chs, eds));
		},
		[setEdges]
	);

	const onConnect: OnConnect = useCallback(
		(params) => setEdges((eds) => addEdge(params, eds)),
		[setEdges]
	);

	return (
		<div style={{width: '100vw', height: '100vh'}}>
			<ReactFlow
				nodes={nodes}
				edges={edges}
				nodeTypes={nodeTypes}
				onNodesChange={onNodesChange}
				onEdgesChange={onEdgesChange}
				onConnect={onConnect}
			/>
		</div>
	);
}