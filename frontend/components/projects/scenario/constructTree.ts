export default function constructTree(data: ScenarioResponse[]) {
	const map = new Map<number, ScenarioResponse>();
	const rootNodes: ScenarioResponse[] = [];

	data.forEach(node => {
		map.set(node.id, node);
		node.children = [];
	});

	data.forEach(node => {
		const parent = map.get(node.parent_id || 0);
		if (parent) {
			parent.children.push(node);
		} else {
			rootNodes.push(node);
		}
	});

	return rootNodes;
}
