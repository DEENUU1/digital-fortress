import {Handle, Position} from 'reactflow';

export function ChildNode({data}: { data: any }) {

	return (
		<>
			<Handle type="target" position={Position.Top}/>
			<div className="bg-black">
				<button className="text-white">Create</button>
				<p className="text-white">xxx</p>
			</div>
			<Handle type="source" position={Position.Bottom} id="a"/>
		</>
	);
}

export function RootNode() {
	return (
		<>
			<div className="bg-black">
				<button className="text-white">Create</button>
			</div>
			<Handle type="source" position={Position.Bottom} id="a"/>
		</>
	)
}